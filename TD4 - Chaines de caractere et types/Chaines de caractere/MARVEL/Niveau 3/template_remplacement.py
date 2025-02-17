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

        # Passage des champs ""texte"" et "lettres_a_remplacer" à la fonction
        texte = data.get("texte", "")
        lettres_a_remplacer = data.get("lettres_a_remplacer", "")
        lettres_de_remplacement = data.get("lettres_de_remplacement", "")
        resultat_utilisateur = user_function(texte, lettres_a_remplacer, lettres_de_remplacement)

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
        "success": False,
        "note": 20,
        "jeux_de_donnees": [
            {
                "name": "Jeu de données visible",
                "data": {
                    "texte": "Les Avengers sont en mission pour récupérer les Pierres d'Infinité avant que Thanos ne les obtienne. Ils doivent s'unir pour protéger l'univers.",
                    "lettres_a_remplacer": "Avangers",
                    "lettres_de_remplacement": "Guardians"
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 15
            },
            {
                "name": "Jeu de test caché 1",
                "data": {
                    "texte": "Natasha et Hawkeye ont combattu l'armée de l'Hydra.",
                    "lettres_a_remplacer": "Natasha",
                    "lettres_de_remplacement": "Natacha"
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            },
            {
                "name": "Jeu de test caché 2",
                "data": {
                    "texte": "Captain America et Hulkkk unissent leurs forces pour sauver la Terre.",
                    "lettres_a_remplacer": "Hulkkk",
                    "lettres_de_remplacement": "Banner"
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
                "name": "Pas de replace",
                "validation": False,
                "message": "Vous avez utilisé la fonction replace, ce qui est interdit.",
                "impact": 20
            },
            {
                "name": "Longueur des séquences",
                "validation": False,
                "message": "Les séquences à remplacer et de remplacement doivent avoir la même longueur.",
                "impact": 10
            },
            {
                "name": "Trop de boucles",
                "validation": False,
                "message": "Vous avez utilisé trop de boucles imbriquées.",
                "impact": 2
            }
        ],
        "bonus": [
            {
                "name": "Gestion des cas invalides",
                "validation": False,
                "message": "Votre code gère correctement les cas où les séquences sont invalides, +2 points !",
                "impact": 2
            },
            {
                "name": "Optimisation avec une seule boucle",
                "validation": False,
                "message": "Vous avez utilisé une seule boucle for pour résoudre l'exercice, +1 points !",
                "impact": 1
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }


    # ETAPE 2: Définition des jeux de données

    def reparo(texte, lettres_a_remplacer, lettres_de_remplacement):
        if len(lettres_a_remplacer) == len(lettres_de_remplacement):
            lon = len(lettres_a_remplacer)
            for i in range(len(texte) - lon + 1):
                if texte[i : i + lon] == lettres_a_remplacer:
                    texte = texte[:i] + lettres_de_remplacement + texte[i + lon :]
        return texte

    for jeu in resultat['jeux_de_donnees']:
        data = jeu["data"]
        jeu["correction"] = reparo(data["texte"], data["lettres_a_remplacer"], data["lettres_de_remplacement"])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(texte, lettres_a_remplacer, lettres_de_remplacement):
        if len(lettres_a_remplacer) == len(lettres_de_remplacement):
            lon = len(lettres_a_remplacer)
            for i in range(len(texte) - lon + 1):
                if texte[i : i + lon] == lettres_a_remplacer:
                    texte = texte[:i] + lettres_de_remplacement + texte[i + lon :]
        return texte"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.

    for contrainte in resultat['contraintes']:
        if contrainte['name'] == "Pas de replace":
            contrainte['validation'] = "replace" not in code_utilisateur
        elif contrainte['name'] == "Longueur des séquences":
            contrainte['validation'] = "if len" in code_utilisateur and "==" in code_utilisateur
        elif contrainte['name'] == "Trop de boucles":
            contrainte['validation'] = code_utilisateur.count("for") <= 2 and code_utilisateur.count("while") == 0

        if not contrainte['validation']:
            append_log(f"Contrainte non respectée: {contrainte['name']}")
            resultat['note'] -= contrainte['impact']
            resultat['note'] = max(0, resultat['note'])
        else:
            append_log(f"Contrainte respectée: {contrainte['name']}")
    
    # ETAPE 4: Définition des bonus de l'exercice.

    for bonus in resultat['bonus']:
        if bonus['name'] == "Gestion des cas invalides":
            bonus['validation'] = "if len" in code_utilisateur and "==" in code_utilisateur
        elif bonus['name'] == "Optimisation avec une seule boucle":
            bonus['validation'] = code_utilisateur.count("for") == 1 and code_utilisateur.count("while") == 0

        if bonus['validation']:
            append_log(f"Bonus obtenu: {bonus['name']}")
            resultat['note'] += bonus['impact']
            resultat['note'] = min(20, resultat['note'])
            


    # ETAPE 5: Run les jeux de données
    for jeu in resultat["jeux_de_donnees"]:
        append_log(f"Exécution du code utilisateur pour le jeu de données {jeu['name']}")
        result = execute_user_code(code_utilisateur, jeu["data"],"reparo")

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

        if not jeu["validation"]:
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
    resultats_file = os.path.join(log_folder, f"resultat-{execution_id}.json")
    try:
        with open(resultats_file, "w") as file:
            json.dump(resultat, file, indent=4)
        append_log(f"Résultats écrits dans le fichier: {resultats_file}")
    except Exception as e:
        append_log(f"Erreur lors de l'écriture du fichier de résultats : {e}")
        print(f"Erreur lors de l'écriture du fichier de résultats : {e}")
