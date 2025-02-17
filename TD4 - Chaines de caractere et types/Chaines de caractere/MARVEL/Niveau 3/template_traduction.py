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
   
    restricted_globals = {}
    local_namespace = {}

    # Redirection de la sortie standard pour capturer le print du code utilisateur
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        # Exécution du code utilisateur dans un espace restreint
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()

        # Récupération de la fonction
        user_function = local_namespace.get(func_name)
        if not user_function:
            raise NameError(f"La fonction '{func_name}' n'a pas été définie dans le code utilisateur.")

        # Passage des champs ""phrase_a_traduire"" et "alphabet" à la fonction
        phrase_a_traduire = data.get("phrase_a_traduire", "")
        alphabet = data.get("alphabet", "")
        alphabet_Skrull = data.get("alphabet_Skrull", "")
        resultat_utilisateur = user_function(phrase_a_traduire, alphabet, alphabet_Skrull)

        return {
            "success": True,
            "output": resultat_utilisateur,
            "console_output": exec_std_output
        }
    except Exception as e:
        # Retourne un dictionnaire décrivant l’erreur
        error_info = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        return {
            "success": False,
            "error": error_info
        }
    finally:
        # Restauration de la sortie standard
        sys.stdout = original_stdout



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
                "name": "Jeu de données visible",
                "data": {
                    "phrase_a_traduire": "ofn Asfpifln qpxnnfpm ofqln gelbfn heql ncqsfl o'qpxsfln",
                    "alphabet": "abcdefghijklmnopqrstuvwxyz",
                    "alphabet_Skrull": "cabdfgizxyvokpehjlnmqstrwu"
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 15
            },
            {
                "name": "Jeu de données caché 1",
                "data": {
                    "phrase_a_traduire": "ofn csfpifln nepm hlêmn heql o'cgglepmfkfpm",
                    "alphabet": "abcdefghijklmnopqrstuvwxyz",
                    "alphabet_Skrull": "cabdfgizxyvokpehjlnmqstrwu"
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
                    "phrase_a_traduire": "rgemgk lmkafut tm lhortkdaf egdzammtfm stl lzoktl rt miafgl",
                    "alphabet": "abcdefghijklmnopqrstuvwxyz",
                    "alphabet_Skrull": "azertyuiopqsdfghjklmwxcvbn"
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            }
        ],
        "contraintes":[
            {
                "name": "Pas de replace",
                "validation": False,
                "message": "Vous avez utilisé la fonction replace. L'exercice n'est pas validé",
                "impact":20
            },
            {
                "name": "Pas de index()",
                "validation": False,
                "message": "Vous ne devez pas utiliser la méthode index() pour rechercher les indices. Utilisez une boucle pour trouver la position des lettres.",
                "impact":15
            },

        ],
        "bonus":[
            {
                "name": "Gestion des cas invalides",
                "validation": False,
                "message": "Votre code gère correctement les entrées invalides, +1 points !",
                "impact": 1
            },
            {
                "name": "Optimisation avec une seule boucle",
                "validation": False,
                "message": "Vous avez utilisé une seule boucle pour résoudre l'exercice, +1 points !",
                "impact": 1
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }
    # ETAPE 2: Définition des jeux de données
    def reparo(phrase_a_traduire, alphabet, alphabet_Skrull):
        phrase_traduite = ""
        for i in range(len(phrase_a_traduire)):
            if phrase_a_traduire[i] in alphabet_Skrull:
                j = 0
                while phrase_a_traduire[i] != alphabet_Skrull[j]:  # pour trouver l'indice de la lettre dans l'alphabet Skrull
                    j += 1
                phrase_traduite = phrase_traduite + alphabet[j]  # à partir de l'indice j, on récupère la lettre correspondante en français
            else:
                phrase_traduite += phrase_a_traduire[i]  # Ajouter les autres caractères (espaces, ponctuation)
        return phrase_traduite

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = reparo(jeu['data']['phrase_a_traduire'], jeu['data']['alphabet'], jeu['data']['alphabet_Skrull'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")



    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(phrase_a_traduire, alphabet, alphabet_Skrull):
        phrase_traduite = ""
        for i in range(len(phrase_a_traduire)):
            if phrase_a_traduire[i] in alphabet_Skrull:
                j = 0
                while phrase_a_traduire[i] != alphabet_Skrull[j]:  # pour trouver l'indice de la lettre dans l'alphabet Skrull
                    j += 1
                phrase_traduite = phrase_traduite + alphabet[j]  # à partir de l'indice j, on récupère la lettre correspondante en français
            else:
                phrase_traduite += phrase_a_traduire[i]  # Ajouter les autres caractères (espaces, ponctuation)
        return phrase_traduite"""
        
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.

    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de replace":
            if "replace" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
        
        # Contrainte index()
        if contrainte['name'] == "Pas de index()":
            if "index" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
        
        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: "+contrainte['name'])
            resultat['note'] = resultat['note'] - contrainte['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']
        else:
            append_log(f"Contrainte respectée: {contrainte}")
    
    
    # ETAPE 4: Définition des bonus de l'exercice.

    for bonus in resultat['bonus']:
        if bonus['name'] == "Optimisation avec une seule boucle":
            if code_utilisateur.count("for") == 1:
                bonus['validation'] = True
        
        if bonus['validation'] == True:
            append_log("Bonus Obtenu: "+bonus['name'])
            resultat['note'] = resultat['note'] + bonus['impact']
            resultat['note'] = 20 if (resultat['note'] > 20) else resultat['note']


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
