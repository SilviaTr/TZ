import json
import traceback
import sys
import io
import os

def append_log(message):
    global log_messages
    log_messages += message + "\n"

def execute_user_code(code, input_data, func_name):
    """
    Exécute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {"stock": input_data}
    restricted_globals = {}

    # Redirection de la sortie standard pour capturer la sortie du code utilisateur
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()
        # Appeler la fonction utilisateur avec les paramètres fournis
        user_function = local_namespace.get(func_name)
        if user_function:
            resultat_utilisateur = user_function(local_namespace["stock"])
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
    output_name = "resultat-" + execution_id + ".json"
    log_folder = "output"

    log_messages = ""

    append_log(f"Nom de la variable de sortie: {output_name}")

    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"logs-{execution_id}.txt")
    append_log("Démarrage de l'exercice")

    resultat = {
        "success": False,
        "note": 20,
        "jeux_de_donnees": [
            {
                "name": "Inventaire principal",
                "input_data": [
                    "Fiction",
                    "Informatique",
                    "Littérature",
                    "Fantasy",
                    "Informatique",
                    "Fiction",
                    "Fantasy",
                    "Littérature",
                    "Fiction",
                    "Informatique",
                    "Fantasy",
                    "Fiction",
                ],
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": {
                    "Fiction": 4,
                    "Informatique": 3,
                    "Littérature": 2,
                    "Fantasy": 3
                },
                "impact": 15
            },
            {
                "name": "Jeu de données caché",
                "input_data": [
                    "Science",
                    "Histoire",
                    "Science",
                    "Fiction",
                    "Histoire",
                    "Science"
                ],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": {
                    "Science": 3,
                    "Histoire": 2,
                    "Fiction": 1
                },
                "impact": 5
            }
        ],
        "contraintes": [
            {
                "name": "Pas de get()",
                "validation": False,
                "message": "Vous avez utilisé la fonction get. L'exercice n'est pas validé.",
                "impact": 20
            }
        ],
        "bonus": [
            {
                "name": "Moins de 2 boucles",
                "validation": False,
                "message": "Vous avez réussi l'exercice avec moins de 2 boucles, +3 points !",
                "impact": 1
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    code_utilisateur = """def faire_inventaire(stock):
    inventaire = {}
    for genre in stock:
        if genre in inventaire:
            inventaire[genre] += 1
        else:
            inventaire[genre] = 1
    return inventaire
    """
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de get()":
            if "get(" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: " + contrainte['name'])
            resultat['note'] -= contrainte['impact']
            resultat['note'] = max(0, resultat['note'])
        else:
            append_log(f"Contrainte respectée: {contrainte}")

    for bonus in resultat['bonus']:
        if bonus['name'] == "Moins de 2 boucles":
            if code_utilisateur.count("for") < 2:
                bonus['validation'] = True

        if bonus['validation'] == True:
            append_log("Bonus Obtenu: " + bonus['name'])
            resultat['note'] += bonus['impact']
            resultat['note'] = min(20, resultat['note'])

    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["input_data"], "faire_inventaire")

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

    try:
        with open(log_file, "w") as f:
            f.write(log_messages)
        append_log(f"Fichier de log écrit avec succès : {log_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de log : {e}")
        print(f"Erreur lors de l'écriture du fichier de log : {e}")

    resultats_file = os.path.join(log_folder, f"resultat-" + execution_id + ".json")
    try:
        with open(resultats_file, "w") as file:
            json.dump(resultat, file, indent=4)
        append_log(f"Résultats écrits dans le fichier: {resultats_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de résultats : {e}")
        print(f"Erreur lors de l'écriture du fichier de résultats : {e}")