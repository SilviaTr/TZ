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


def execute_user_code(code, input_L):
    """
    Execute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {"L": input_L}
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
                "L": [8.5, 24.2, 48.7, 2.1, 16.3, 32.5, 60.0, 15.8, 75.4, 3.9, 21.6, 99.3, 57.8, 80.1, 45.5, 10.2, 63.7, 28.4, 39.9, 88.6, 71.2],
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 14
            },
            {
                "name": "Jeu de données caché 1",
                "L": [8.5, -2, 48.7, 2.1, 16.3, 32.5, 60.0, 1000, 75.4, 3.9, 1000, 99.3, 57.8, 80.1, 45.5, 10.2, 63.7, 28.4, -2, 88.6, 71.2],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            },
            {
                "name": "Jeu de données caché 2",
                "L": [1,1,1,1,1,1],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            }
        ],
        "contraintes": [
            {
                "name": "Pas de min()",
                "validation": False,
                "message": "Vous avez utilisé la fonction min(). L'exercice n'est pas validé",
                "impact": 20
            },
            {
                "name": "Pas de max()",
                "validation": False,
                "message": "Vous avez utilisé la fonction min(). L'exercice n'est pas validé",
                "impact": 20
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }


    # ETAPE 2: Définition des jeux de données
    def input_function(input):
        max =input[0]
        min = input[0]
        for i in  input:
            if i > max :
                max = i
            else :
                if i < min :
                        min = i
        return (min, max)


    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = input_function((jeu['L']))

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """
def min_max(input):
     max =input[0]
     min = input[0]
     for i in  input:
          if i > max :
               max = i
          else :
               if i < min :
                    min = i
     return (min, max)

output=min_max(L)
print(output)
"""

    append_log(f"Code utilisateur: {code_utilisateur}")

    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        # Contrainte de replace
        if contrainte['name'] == "Pas de min()":
            if "min" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        # Contrainte trop de if
        if contrainte['name'] == "Pas de max()":
            if "max" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: " + contrainte['name'])
            resultat['note'] = resultat['note'] - contrainte['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']
        else:
            append_log(f"Contrainte respectée: {contrainte}")
    # ETAPE 4: Définition des bonus de l'exercice.

    # ETAPE 5: Run les jeux de données
    # Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["L"])

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
