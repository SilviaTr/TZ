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


def execute_user_code(code, input_message_secret, input_permutations):
    """
    Execute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {"message_secret": input_message_secret, "permutations": input_permutations}
    restricted_globals = {}

    # Redirection de la sortie standard pour capturer la sortie du code utilisateur
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()
        # Vérification si le code utilisateur a défini 'output' dans l'espace de nom local
        resultat_utilisateur = local_namespace.get("output")
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
        # Rétablissement de la sortie standard
        sys.stdout = original_stdout


if __name__ == "__main__":
    execution_id = "REPLACE_ME_EXECUTION_ID"
    output_name = "resultat-" + execution_id + ".json"
    log_folder = "output"

    log_messages = ""

    append_log(f"Nom de la variable de sortie: {output_name}")

    # Configuration des logs
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"logs-{execution_id}.txt")
    append_log("Démarrage de l'exercice")

    # ETAPE 1 : Resultat json
    resultat = {
        "success": False,
        "note": 20,
        "jeux_de_donnees": [
            {
                "name": "Liste initiale",
                "message_secret": ["t", "o", "m", " ", "e", "l", "v", "i", "s", " ", "j", "e", "d", "u", "s", "o", "r"],
                "permutations": [[10, 0], [4, 1], [3, 2], [8, 3], [13, 4], [7, 5], [14, 6], [9, 7], [14, 8], [13, 9], [13, 10], [12, 11], [14, 13], [15, 14], [16, 15]],
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 10
            },
            {
                "name": "Jeu de données caché 1",
                "message_secret": ["h", "a", "r", "r", "y", " ", "p", "o", "t", "t", "e", "r", " ", "v", "i", "v", "a", "n", "t"],
                "permutations": [[8, 0], [2, 1], [7, 2], [11, 3], [9, 4], [6, 5], [10, 6],[5, 7], [12, 8], [13, 9], [14, 10], [15, 11], [13, 12], [14, 13], [15, 14]],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 5
            },
            {
                "name": "Jeu de données caché 2",
                "message_secret": ["h", "e", "r", "m", "i", "o", "n", "e", " ", "g", "r", "a", "n", "g", "e", "r"],
                "permutations": [[12, 0], [7, 1], [5, 2], [10, 3], [13, 4], [3, 5], [15, 6], [8, 7], [16, 8], [11, 9], [14, 10], [17, 11], [18, 12], [15, 13], [16, 14]],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 5
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }


    # ETAPE 2: Définition des jeux de données
    def input_function(input):
        message_decode=input[0]
        permutations = input[1]
        for permutation in permutations:
            tmp = message_decode[permutation[1]]
            message_decode[permutation[1]] = message_decode[permutation[0]]
            message_decode[permutation[0]] = tmp
        return message_decode

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = input_function((jeu['message_secret'],jeu['permutations'] ))

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """
def permutation(input):
    message_decode=input[0]
    permutations = input[1]
    for permutation in permutations:
        tmp = message_decode[permutation[1]]
        message_decode[permutation[1]] = message_decode[permutation[0]]
        message_decode[permutation[0]] = tmp
    return message_decode

output=permutation((message_secret, permutations))
print(output)
"""

    append_log(f"Code utilisateur: {code_utilisateur}")

    # Étape 3: Définition des contraintes de l'exercice.

    # ETAPE 4: Définition des bonus de l'exercice.

    # ETAPE 5: Run les jeux de données
    # Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["message_secret"], jeu["permutations"])

        if result["success"]:
            jeu["resultat_utilisateur"] = result["output"]
            append_log(f"Résultat du code utilisateur: {result['output']}")

            # Comparaison avec la correction attendue
            if result["output"] == jeu["correction"]:
                jeu["validation"] = True
                append_log(f"Validation réussie pour le jeu de données {jeu['name']}.")
            else:
                jeu["validation"] = False
                append_log(
                    f"Validation échouée pour le jeu de données {jeu['name']}. Résultat attendu: {jeu['correction']}, obtenu: {result['output']}")
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
