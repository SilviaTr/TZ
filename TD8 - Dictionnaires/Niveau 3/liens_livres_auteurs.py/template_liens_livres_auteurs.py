import json
import traceback
import sys
import io
import os

def append_log(message):
    global log_messages
    log_messages += message + "\n"

def execute_user_code(code, func_name, input_data):
    """
    Exécute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {}
    restricted_globals = {}

    # Redirection de la sortie standard pour capturer la sortie du code utilisateur
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()
        user_function = local_namespace.get(func_name)
        if user_function:
            # Déterminer les paramètres à passer en fonction du nom de la fonction
            if func_name == "genre_predilection":
                resultat_utilisateur = user_function(input_data["livres"], input_data["auteur"])
            else:
                resultat_utilisateur = user_function(input_data["livres"])
        else:
            raise NameError(f"La fonction {func_name} n'a pas été définie par l'utilisateur.")
        return {"success": True, "output": resultat_utilisateur, "console_output": exec_std_output}
    except Exception as e:
        error_info = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        return {"success": False, "error": error_info}
    finally:
        sys.stdout = original_stdout

if __name__ == "__main__":
    execution_id = "REPLACE_ME_EXECUTION_ID"
    output_name = "result-"+execution_id+".json"
    log_folder = "output"

    log_messages = ""

    append_log(f"Nom de la variable de sortie: {output_name}")

    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"logs-{execution_id}.txt")
    append_log("Démarrage de l'exercice")

    resultat = "REPLACE_ME_RESULT_OBJECT"

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    code_utilisateur = """REPLACE_ME_CODE_UTILISATEUR"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    
    # Étape 2: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de get()":
            if "get(" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['name'] == "Pas de max()":
            if "max(" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: " + contrainte['name'])
            resultat['note'] -= contrainte['impact']
            resultat['note'] = max(0, resultat['note'])
        else:
            append_log(f"Contrainte respectée: {contrainte}")

    # ETAPE 4: Définition des bonus de l'exercice.
    for bonus in resultat['bonus']:
        if bonus['name'] == "Moins de 3 boucles":
            if code_utilisateur.count("for") < 3:
                bonus['validation'] = True

        if bonus['validation'] == True:
            append_log("Bonus Obtenu: " + bonus['name'])
            resultat['note'] += bonus['impact']
            resultat['note'] = min(20, resultat['note'])

    # ETAPE 5: Run les jeux de données
    # Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        function_name_map = {
            "Genre de prédilection": "genre_predilection",
            "Auteur de Fiction": "auteur_fiction",
            "Auteur des livres les plus longs": "auteur_livres_longs"
        }
        func_name = function_name_map[jeu['name']]
        result = execute_user_code(code_utilisateur, func_name, jeu["input_data"])

        if result["success"]:
            jeu["resultat_utilisateur"] = result["output"]
            append_log(f"Résultat du code utilisateur: {result['output']}")

            if result["output"] == jeu["correction"]:
                jeu["validation"] = True
                append_log(f"Validation réussie pour le jeu de données {jeu['name']}.")
            else:
                jeu["validation"] = False
                append_log(f"Validation échouée pour le jeu de données {jeu['name']}. Résultat attendu: {jeu['correction']}, obtenu: {result['output']}")
        else:
            jeu["validation"] = False
            jeu["resultat_utilisateur"] = None
            resultat['console']['type'] = "error"
            resultat['console']['message'].append(result["error"])
            append_log(f"Erreur rencontrée: {result['error']['type']} - {result['error']['message']}")
            append_log(f"Traceback: {result['error']['traceback']}")

        if jeu["validation"] == False:
            resultat['note'] -= jeu['impact']
            resultat['note'] = max(0, resultat['note'])

    append_log("Fin de l'exercice")
    
# ETAPE 6 : Ecriture du resultat

    # Sauvegarde des logs
    try:
        with open(log_file, "w") as f:
            f.write(log_messages)
        append_log(f"Fichier de log écrit avec succès : {log_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de log : {e}")
        print(f"Erreur lors de l'écriture du fichier de log : {e}")

    # Sauvegarde des résultats dans un fichier JSON
    resultats_file = os.path.join(log_folder, f"result-{execution_id}.json")
    try:
        with open(resultats_file, "w") as file:
            json.dump(resultat, file, indent=4)
        append_log(f"Résultats écrits dans le fichier: {resultats_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de résultats : {e}")
        print(f"Erreur lors de l'écriture du fichier de résultats : {e}")