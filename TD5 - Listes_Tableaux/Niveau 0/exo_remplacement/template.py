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


def execute_user_code(code, input_data):
    """
    Execute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {"input": input_data}
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
                "name": "Liste_initiale",
                "data": ['a', 'b', 'c', 'd', 'u', 'v', 'w','e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w','c', 'x', 'y', 'z', 'c','c', 'x', 'y','n', 'o', 'p'],
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 14
            },
            {
                "name": "Jeu de données caché 1",
                "data": ['c', 'c', 'c', 'c', 'c', 'c', 'c','c', 'c'],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            },
            {
                "name": "Jeu de données caché 2",
                "data":  ['w', 'w', 'w', 'w', 'c', 'w', 'w','w', 'w', 'w', 'w'],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            }
        ],
        "contraintes": [
            {
                "name": "Pas de append",
                "validation": False,
                "message": "Vous avez utilisé la fonction append. L'exercice n'est pas validé",
                "impact": 20
            },
            {
                "name": "Pas de remove",
                "validation": False,
                "message": "Vous avez utilisé la fonction remove. L'exercice n'est pas validé",
                "impact": 15
            }
        ],
        "bonus": [],
        "console": {
            "type": None,
            "message": []
        }
    }


    # ETAPE 2: Définition des jeux de données
    def input_function(input):
        for k in range(len(input)):
            if input[k] == 'c':
                input[k] = 'w'
        return input

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = input_function(jeu['data'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """
def remplacement(lettres):
    for k in range(len(lettres)):
        if lettres[k] == 'c':
            lettres[k] = 'w'
    return lettres

output = remplacement(input)
print(output)
"""

    append_log(f"Code utilisateur: {code_utilisateur}")

    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de append":
            if "append" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['name'] == "Pas de remove":
            if "remove" in code_utilisateur:
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
    for bonus in resultat['bonus']:
        # Contrainte de replace
        if bonus['name'] == "Moins de 2 for":
            if code_utilisateur.count("for") < 2:
                bonus['validation'] = True

        if bonus['validation'] == True:
            append_log("Bonus Obtenu: " + bonus['name'])
            resultat['note'] = resultat['note'] + bonus['impact']
            resultat['note'] = 20 if (resultat['note'] > 20) else resultat['note']

    # ETAPE 5: Run les jeux de données
    # Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["data"])

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
