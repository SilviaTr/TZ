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
        "collection": data["collection"],
        "figurines_disponibles": data.get("figurines_disponibles", [])
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
            resultat_utilisateur = user_function(local_namespace["collection"],local_namespace["figurines_disponibles"])  # Passer les bonnes variables
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
    "success": False,
    "note": 20,
    "jeux_de_donnees": [
        {
            "name": "Collection de figurines 1",
            "data": {
                "collection": [
                    "Iron Man", "Captain America", "Thor", "Black Widow", "Hulk", 
                    "Thor", "Spider-Man", "Iron Man", "Doctor Strange", 
                    "Black Widow", "Hawkeye", "Hawkeye", "Thor", "Vision"
                ],
                "figurines_disponibles" : [
                    "Black Panther","Iron Man","Captain America","Spider-Man","Thor",
                    "Black Widow","Doctor Strange","Hulk","Scarlet Witch","Vision",
                    "Groot","Wolverine","Hawkeye","Deadpool"
                ]
            },
            "hidden": False,
            "validation": False,
            "resultat_utilisateur": "",
            "correction": [
                ["Thor","Iron Man", "Black Widow", "Hawkeye"],
                ["Iron Man", "Captain America", "Thor", "Black Widow", "Hulk", "Spider-Man", "Doctor Strange", "Hawkeye", "Vision"],
                ["Black Panther", "Scarlet Witch", "Groot", "Wolverine", "Deadpool"]
            ],
            "impact": 15
        },
        {
            "name": "Collection de figurines cachée 2",
            "data": {
                "collection": [
                    "Black Panther", "Black Panther"
                ]
            },
            "hidden": True,
            "validation": False,
            "resultat_utilisateur": "",
            "correction": [
                ["Black Panther"],
                ["Black Panther"],
                []
            ],
            "impact": 3
        },
        {
            "name": "Collection de figurines cachée 3",
            "data": {
                "collection": [
                    "Iron Man", "Black Panther", "Hawkeye", "Wolverine", "Thor",
                    "Black Widow", "Vision", "Scarlet Witch", "Hulk", "Groot"
                ],
                "figurines_disponibles" : [
                    "Black Panther", "Iron Man", "Captain America", "Spider-Man", "Thor",
                    "Black Widow", "Doctor Strange", "Hulk", "Scarlet Witch", "Vision",
                    "Groot", "Wolverine", "Hawkeye", "Deadpool"
                ]
            },
            "hidden": True,
            "validation": False,
            "resultat_utilisateur": "",
            "correction": [
                [],
                ["Iron Man", "Black Panther", "Hawkeye", "Wolverine", "Thor", "Black Widow", "Vision", "Scarlet Witch", "Hulk", "Groot"],
                [
                    "Captain America", "Spider-Man", "Doctor Strange", "Deadpool"
                ]
            ],
            "impact": 2
        }
    ],
        "contraintes": [

            {
                "name": "Pas d'utilisation de set",
                "validation": False,
                "message": "L'utilisation de structures de données comme 'set' est interdite. Vous devez gérer les doublons manuellement.",
                "impact": 5
            },
            {
                "name": "Pas d'utilisation de fonctions externes comme join, map, filter",
                "validation": False,
                "message": "L'utilisation des fonctions 'join()', 'map()', ou 'filter()' est interdite dans cet exercice. Vous devez utiliser une simple boucle.",
                "impact": 5
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }


    # Le code utilisateur est injecté ici
    code_utilisateur = '''def reparo(collection, figurines_disponibles):
    def detect_doublons(collection):
        doublons = []
        figurines_classees = []
        for figurine in collection:
            if figurine in figurines_classees and figurine not in doublons:
                doublons.append(figurine)
            figurines_classees.append(figurine)
        return doublons

    def collection_unique(collection):
        collection_sans_doublons = []
        for figurine in collection:
            if figurine not in collection_sans_doublons:
                collection_sans_doublons.append(figurine)
        return collection_sans_doublons

    def figurines_manquantes(collection, figurines_disponibles):
        return [figurine for figurine in figurines_disponibles if figurine not in collection]

    # Retourner les trois résultats sous forme de listes uniques
    doublons = detect_doublons(collection)
    collection_sans_doublons = collection_unique(collection)
    figurines_pas_dans_collection = figurines_manquantes(collection, figurines_disponibles)

    return [doublons, collection_sans_doublons, figurines_pas_dans_collection]
'''
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice
    for contrainte in resultat['contraintes']:



        # Contrainte : Pas d'utilisation de 'set'
        if contrainte['name'] == "Pas d'utilisation de set":
            if "set" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        # Contrainte : Pas d'utilisation de fonctions externes comme 'join', 'map', 'filter'
        if contrainte['name'] == "Pas d'utilisation de fonctions externes comme join, map, filter":
            if "join" in code_utilisateur or "map" in code_utilisateur or "filter" in code_utilisateur:
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
