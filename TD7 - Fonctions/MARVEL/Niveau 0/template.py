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
        "texte": data["texte"],
        "nb_fois": data["nb_fois"]
    } 
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
            resultat_utilisateur = user_function(local_namespace["texte"], local_namespace["nb_fois"])  # Passer les bonnes variables
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
                "name": "Lettre à décoder",
                "data": {
                    "texte": "La clé de la défense avancée réside dans la technologie. Comme Tony Stark le dit souvent, 'Une technologie bien pensée vaut mieux que dix super-soldats.' \
                    La préparation implique de connaître les systèmes défensifs, les contre-mesures automatiques et les moyens de renforcer la sécurité autour des Avengers. \
                    Un Avenger bien équipé est prêt à faire face aux menaces, qu'elles viennent de l'espace ou de la Terre. Un autre principe clé de la défense avancée est la concentration. \
                    Dans les situations de crise, il est crucial de se concentrer sur la menace immédiate. Les systèmes défensifs demandent une précision extrême, \
                    et toute distraction pourrait être fatale. Les Avengers doivent rester focalisés, même sous pression, car cela peut signifier la différence entre sauver la planète ou la perdre.",
                    "nb_fois": 3
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "La clé de la défense avancée réside dans la technologie. Comme Tony Stark le dit souvent, 'Une technologie bien pensée vaut mieux que dix super-soldats.' \
                    La préparation implique de connaître les systèmes défensifs, les contre-mesures automatiques et les moyens de renforcer la sécurité autour des Avengers. \
                    Un Avenger bien équipé est prêt à faire face aux menaces, qu'elles viennent de l'espace ou de la Terre. Un autre principe clé de la défense avancée est la concentration. \
                    Dans les situations de crise, il est crucial de se concentrer sur la menace immédiate. Les systèmes défensifs demandent une précision extrême, \
                    et toute distraction pourrait être fatale. Les Avengers doivent rester focalisés, même sous pression, car cela peut signifier la différence entre sauver la planète ou la perdre\
                    La clé de la défense avancée réside dans la technologie. Comme Tony Stark le dit souvent, 'Une technologie bien pensée vaut mieux que dix super-soldats.' \
                    La préparation implique de connaître les systèmes défensifs, les contre-mesures automatiques et les moyens de renforcer la sécurité autour des Avengers. \
                    Un Avenger bien équipé est prêt à faire face aux menaces, qu'elles viennent de l'espace ou de la Terre. Un autre principe clé de la défense avancée est la concentration. \
                    Dans les situations de crise, il est crucial de se concentrer sur la menace immédiate. Les systèmes défensifs demandent une précision extrême, \
                    et toute distraction pourrait être fatale. Les Avengers doivent rester focalisés, même sous pression, car cela peut signifier la différence entre sauver la planète ou la perdre.\
                    La clé de la défense avancée réside dans la technologie. Comme Tony Stark le dit souvent, 'Une technologie bien pensée vaut mieux que dix super-soldats. \
                    La préparation implique de connaître les systèmes défensifs, les contre-mesures automatiques et les moyens de renforcer la sécurité autour des Avengers. \
                    Un Avenger bien équipé est prêt à faire face aux menaces, qu'elles viennent de l'espace ou de la Terre. Un autre principe clé de la défense avancée est la concentration. \
                    Dans les situations de crise, il est crucial de se concentrer sur la menace immédiate. Les systèmes défensifs demandent une précision extrême, \
                    et toute distraction pourrait être fatale. Les Avengers doivent rester focalisés, même sous pression, car cela peut signifier la différence entre sauver la planète ou la perdre.",
                "correction": "",
                "impact": 15
            },
            {
                "name": "Jeu de données caché 1",
                "data": {
                    "texte": "Le Captain America porte son bouclier indestructible, qu'il utilise pour defendre les innocents contre les menaces. Son courage est sans égal et il inspire tout les Avengers.",
                    "nb_fois": 2
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 2
            },
            {
                "name": "Jeu de données caché 2",
                "data": {
                    "texte": "a",
                    "nb_fois": 10
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 2
            }
        ],
        "contraintes": [
            {
                "name": "Pas de while ou do-while",
                "validation": False,
                "message": "L'utilisation de la boucle 'while' ou 'do-while' est interdite. Vous devez utiliser une boucle 'for'.",
                "impact": 10
            },
            {
                "name": "Pas de manipulation des indices",
                "validation": False,
                "message": "Vous ne devez pas manipuler directement les indices de la boucle pour répéter le texte. Utilisez directement une boucle 'for' avec 'range(n)'.",
                "impact": 5
            },
            {
                "name": "Limiter l'utilisation des fonctions externes",
                "validation": False,
                "message": "Vous ne devez pas utiliser des fonctions externes telles que 'join()' ou 'map()' pour cette tâche. L'objectif est de recourir uniquement à une simple boucle.",
                "impact": 5
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }

    # ETAPE 2: Définition des jeux de données
    def reparo(texte, nb_fois):
        solution = ""
        for i in range(nb_fois):
            solution += texte
            solution += " - "
        return solution

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = reparo(jeu['data']['texte'], jeu['data']['nb_fois'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")



    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(texte, n):
    solution = ""
    for i in range(n):
        solution += texte
        solution += " - "
    return solution"""

    
    append_log(f"Code utilisateur: {code_utilisateur}")

    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de while ou do-while":
            if "while" in code_utilisateur or "do" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['name'] == "Pas de manipulation des indices":
            if "[" in code_utilisateur or "index" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['name'] == "Limiter l'utilisation des fonctions externes":
            if "join" in code_utilisateur or "map" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: " + contrainte['name'])
            resultat['note'] = resultat['note'] - contrainte['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']
        else:
            append_log(f"Contrainte respectée: {contrainte}")

    # ETAPE 5: Exécution des jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["data"], "reparo")

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
