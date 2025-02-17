import json
import random
import copy
import re
import traceback
import sys
import io
import os

def append_log(message):
    global log_messages
    log_messages += message + "\n"

def execute_user_code(code, data, func_name):
    """
    Exécute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    
    local_namespace = {
        "message": data["message"],
        "lettre_a_remplacer": data["lettre_a_remplacer"],
        "lettre_de_remplacement": data["lettre_de_remplacement"]} 
    restricted_globals = {}

    # Redirection de la sortie standard pour capturer la sortie du code utilisateur
    originale_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        # Exécution du code avec les variables définies
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()
        # Appeler la fonction utilisateur avec les paramètres fournis
        user_function = local_namespace.get(func_name)
        if user_function:
            resultat_utilisateur = user_function(local_namespace["message"], local_namespace["lettre_a_remplacer"],local_namespace["lettre_de_remplacement"])  # Passer les bonnes variables
        else:
            raise NameError(f"La fonction {func_name} n'a pas été définie par l'utilisateur.")
        return {"success": True, "output": resultat_utilisateur, "console_output": exec_std_output}
    except Exception as e:
        # En cas d'erreur, retourner les détails de l'exception
        error_info = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        return {"success": False, "error": error_info}
    finally:
        sys.stdout = originale_stdout


if __name__ == "__main__":
    execution_id = "REPLACE_ME_EXECUTION_ID"
    output_name = "resultat-"+execution_id+".json"
    log_folder = "output"

    log_messages = ""

    append_log(f"Nom de la variable de sortie: {output_name}")

    # Configuration des logs
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"logs-{execution_id}.txt")
    append_log("Démarrage de l'exercice")

    # ETAPE 1 : Resultat json
    resultat = {
        "success":False,
        "note":20,
        "jeux_de_donnees":[ 
            {
                "name": "Message codé 1",
                "data": {
                    "message": "Tony Staxk cxée des axmures poux pxotéger le monde",
                    "lettre_a_remplacer": "x",
                    "lettre_de_remplacement": "r"
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "Tony Stark crée des armures pour protéger le monde",
                "impact": 15
            },
            {
                "name": "Message codé 2",
                "data": {
                    "message": "Thor manix son martxau avxc unx forcx divinx",
                    "lettre_a_remplacer": "x",
                    "lettre_de_remplacement": "e"
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "Thor manie son marteau avec une force divine",
                "impact": 3
            },
            {
                "name": "Message codé 3",
                "data": {
                    "message": "Hulk imaih tout sur ion paiiage !",
                    "lettre_a_remplacer": "i",
                    "lettre_de_remplacement": "s"
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "Hulk smash tout sur son passage !",
                "impact": 2
            }
        ],
        "contraintes": [
            {
                "name": "Pas de 'replace'",
                "validation": False,
                "message": "L'utilisation de la fonction 'replace' est interdite. Utilisez une boucle pour remplacer les lettres.",
                "impact": 10
            },
            {
                "name": "Pas de 'in'",
                "validation": False,
                "message": "L'utilisation de 'in' est interdite dans cet exercice.",
                "impact": 4
            },
            {
                "name": "Limitation des boucles 'for'",
                "validation": False,
                "message": "Vous ne devez pas utiliser plus de 2 boucles 'for'.",
                "impact": 5
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }



    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(message, lettre_a_remplacer, lettre_de_remplacement):
    message_decode = message
    for i in range(len(message_decode)):
        if message_decode[i] == lettre_a_remplacer:
            message_decode = (
                message_decode[:i] + lettre_de_remplacement + message_decode[i + 1 :]
            )
    return message_decode"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice
    for contrainte in resultat['contraintes']:

        # Contrainte : Pas d'utilisation de 'replace'
        if contrainte['name'] == "Pas de 'replace'":
            if "replace" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        # Contrainte : Pas d'utilisation de 'in' sauf dans 'for i in range'
        if contrainte['name'] == "Pas de 'in'":
            if " in " in code_utilisateur:
                # Vérifie si 'in' est utilisé dans une boucle for sans 'range', ce qui est interdit
                if "in range" in code_utilisateur:
                    contrainte['validation'] = True
                else:
                    contrainte['validation'] = True
            else:
                contrainte['validation'] = True

        # Contrainte : Limitation des boucles 'for'
        if contrainte['name'] == "Limitation des boucles 'for'":
            if code_utilisateur.count("for") > 2:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

            

        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: " + contrainte['name'])
            resultat['note'] = resultat['note'] - contrainte['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']
        else:
            append_log(f"Contrainte respectée: {contrainte}")

        

    # ETAPE 5: Run les jeux de données
    # Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["data"],"reparo")

        if result["success"]:
            jeu["resultat_utilisateur"] = result["output"]
            append_log(f"Résultat du code utilisateur: {result['output']}")

            # Comparaison avec la correction attendue
            if result["output"] == jeu["correction"]:
                jeu["validation"] = True
                append_log(f"Validation réussie pour le jeu de données {jeu['name']}.")
            else:
                jeu["validation"] = False
                append_log(f"Validation échouée pour le jeu de données {jeu['name']}. Résultat attendu: {jeu['correction']}, obtenu: {result['output']}")
        else:
            # En cas d'erreur, mettre à jour les champs et logger l'erreur
            jeu["validation"] = False
            jeu["resultat_utilisateur"] = None
            resultat['console']['type'] = "error"
            resultat['console']['message'].append(result["error"])
            append_log(f"Erreur rencontrée: {result['error']['type']} - {result['error']['message']}")
            append_log(f"Traceback: {result['error']['traceback']}")
        
        if jeu["validation"] == False:
            resultat['note'] = resultat['note'] - jeu['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']

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
    resultats_file = os.path.join(log_folder, f"resultat-{execution_id}.json")
    try:
        with open(resultats_file, "w") as file:
            json.dump(resultat, file, indent=4)
        append_log(f"Résultats écrits dans le fichier: {resultats_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de résultats : {e}")
        print(f"Erreur lors de l'écriture du fichier de résultats : {e}")
