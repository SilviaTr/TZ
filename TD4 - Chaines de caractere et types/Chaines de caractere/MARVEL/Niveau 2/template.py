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
                    "texte": "Lew Avengerw, un groupe de herow venuw de touw les horizonw, we preparent à affronter Thanow danw un combat épique. Leur miwwion : wauver l'univerw et retablir l'equilibre de la galaxie.",
                    "lettre_a_remplacer": "w",
                    "lettre_de_remplacement": "s"
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "Les Avengers, un groupe de heros venus de tous les horizons, se preparent à affronter Thanos dans un combat épique. Leur mission : sauver l'univers et retablir l'equilibre de la galaxie.",
                "impact": 15
            },
            {
                "name": "Jeu de test caché 1",
                "data": {
                    "texte": "Lz cizl pzt blzu, l'air zst pur.",
                    "lettre_a_remplacer": "z",
                    "lettre_de_remplacement": "e"
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
                    "texte": "Le zuper-héroz ezt prêt à zaver le monde.",
                    "lettre_a_remplacer": "z",
                    "lettre_de_remplacement": "s"
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "Le super-héros est prêt à sauver le monde.",
                "impact": 2
            }
        ],
        "contraintes": [
            {
                "name": "Pas de replace",
                "validation": False,
                "message": "Vous avez utilisé la fonction replace. L'exercice n'est pas validé.",
                "impact": 20
            },
            {
                "name": "Trop de if",
                "validation": False,
                "message": "Vous avez utilisé trop de conditions if. Limitez-vous à 2 maximum. -3points",
                "impact": 3
            }
        ],
        "bonus": [
            {
                "name": "Gestion des cas invalides",
                "validation": False,
                "message": "Votre code gère correctement les entrées invalides, +1 points !",
                "impact":1
            },
            {
                "name": "Optimisation avec une seule boucle",
                "validation": False,
                "message": "Vous avez utilisé moins de 2 boucles, +1 points !",
                "impact": 1
            }
        ],
        "console": {
            "type": None,
            "message": []
        }
    }

    # ETAPE 2: Définition des jeux de données

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(texte, lettre_a_remplacer, lettre_de_remplacement):
        for i in range(len(texte)):
            if texte[i] == lettre_a_remplacer:
                texte = texte[:i] + lettre_de_remplacement + texte[i + 1:]
        return texte"""
        
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        # Contrainte de replace
        if contrainte['name'] == "Pas de replace":
            if "replace" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
        
        # Contrainte trop de if
        if contrainte['name'] == "Trop de If":
            if code_utilisateur.count("if") > 2:
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
    # ETAPE 4: Définition des bonus de l'exercice.
    for bonus in resultat['bonus']:
        # Bonus "Gestion des cas invalides"
        if bonus['name'] == "Gestion des cas invalides":
            if "if len" in code_utilisateur and "-1" in code_utilisateur:
                bonus['validation'] = True

        # Bonus "Optimisation avec une seule boucle"
        elif bonus['name'] == "Optimisation avec une seule boucle":
            total_boucles = code_utilisateur.count("for") + code_utilisateur.count("while")
            if total_boucles <= 1:
                bonus['validation'] = True

        # Gestion des logs et ajustement de la note
        if bonus['validation']:
            append_log(f"Bonus obtenu : {bonus['name']} - {bonus['message']}")
            resultat['note'] += bonus['impact']
            resultat['note'] = min(20, resultat['note'])  # Assure que la note ne dépasse pas 20


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
