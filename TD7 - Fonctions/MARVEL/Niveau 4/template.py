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
        "phrase": data["phrase"],
        "longeur": data.get("longeur", [])
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
            resultat_utilisateur = user_function(local_namespace["phrase"],local_namespace["longeur"])  # Passer les bonnes variables
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
            "name": "Jeu de données visible",
            "data": {
                "phrase": "Iron Man et Captain America combattent ensemble contre Thanos et ses alliés.",
                "longeur" : 6
            },
            "hidden": False,
            "validation": False,
            "resultat_utilisateur": "",
            "correction":"",
            "impact": 15
        },
        {
            "name": "Jeu de test caché",
            "data": {
                "phrase": "Spider-Man se bat contre Green Goblin et Doctor Octopus à New York.",
                "longeur": "5"
            },
            "hidden": True,
            "validation": False,
            "resultat_utilisateur": "",
            "correction":"",
            "impact": 3
        },
        {
            "name": "Jeu de test caché",
            "data": {
                "phrase": "",
                "longeur" : 19
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
                "name": "Pas d'utilisation de set",
                "validation": False,
                "message": "L'utilisation de structures de données comme 'set' est interdite. Vous devez gérer les doublons manuellement.",
                "impact": 5
            },
            {
                "name": "Pas d'utilisation de fonctions externes comme  map, filter",
                "validation": False,
                "message": "L'utilisation des fonctions 'map()', ou 'filter()' est interdite dans cet exercice. Vous devez utiliser une simple boucle.",
                "impact": 5
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }
    
    # ETAPE 2: Définition des jeux de données

    def reparo(phrase, longueur):
        def compter_mots(phrase):
            mots = phrase.split()
            return len(mots)

        def inverser_phrase(phrase):
            mots = phrase.split()
            mots_inverse = mots[::-1]
            phrase_inverse = ' '.join(mots_inverse)
            return phrase_inverse

        def trouver_mots_longueur(phrase, longueur):
            mots = phrase.split()
            mots_filtres = [mot for mot in mots if len(mot) == longueur]
            return mots_filtres

        # Exécution des différentes fonctions
        nombre_de_mots = compter_mots(phrase)
        phrase_inversee = inverser_phrase(phrase)
        mots_de_longueur_specifiee = trouver_mots_longueur(phrase, longueur) if longueur is not None else []

        # Retourner les résultats sous forme de tuple
        return nombre_de_mots, phrase_inversee, mots_de_longueur_specifiee
    
    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = reparo(jeu['data']['phrase'], jeu['data']['longeur'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(phrase, longueur):
        def compter_mots(phrase):
            mots = phrase.split()
            return len(mots)

        def inverser_phrase(phrase):
            mots = phrase.split()
            mots_inverse = mots[::-1]
            phrase_inverse = ' '.join(mots_inverse)
            return phrase_inverse

        def trouver_mots_longueur(phrase, longueur):
            mots = phrase.split()
            mots_filtres = [mot for mot in mots if len(mot) == longueur]
            return mots_filtres

        # Exécution des différentes fonctions
        nombre_de_mots = compter_mots(phrase)
        phrase_inversee = inverser_phrase(phrase)
        mots_de_longueur_specifiee = trouver_mots_longueur(phrase, longueur) if longueur is not None else []

        # Retourner les résultats sous forme de tuple
        return nombre_de_mots, phrase_inversee, mots_de_longueur_specifiee"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice
    for contrainte in resultat['contraintes']:



        # Contrainte : Pas d'utilisation de 'set'
        if contrainte['name'] == "Pas d'utilisation de set":
            if "set" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        # Contrainte : Pas d'utilisation de fonctions externes comme 'map', 'filter'
        if contrainte['name'] == "Pas d'utilisation de fonctions externes comme  map, filter":
            if  "map" in code_utilisateur or "filter" in code_utilisateur:
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
