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
                "name": "ordre_attaque",
                "data": [ "L'heure", "de", "la", "destruction", "est", "venue.", "Envoyez", "toutes",
    "les", "flottes", "vers", "la", "Terre.", "Aucune", "pitié", "ne", "sera",
    "accordée.", "Notre", "armada", "écrasera", "chaque", "résistance.", "Déployez",
    "les", "vaisseaux", "sur", "les", "points", "stratégiques,", "anéantissez",
    "les", "cités", "majeures,", "et", "assurez-vous", "que", "les", "Avengers",
    "ne", "puissent", "pas", "intervenir.", "La", "planète", "doit", "tomber",
    "sous", "notre", "contrôle", "avant", "la", "fin", "du", "jour.", "Nous",
    "dominerons", "cet", "univers."],
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 14
            },
            {
                "name": "Jeu de données caché 1",
                "data": [
    "Ici", "le", "capitaine", "du", "vaisseau", "Eclipse.", "Nous", "sommes",
    "sous", "attaque", "et", "nos", "boucliers", "sont", "compromis.", "Nous",
    "demandons", "une", "assistance", "immédiate", "de", "toute", "force",
    "alliée", "à", "portée.", "Sans", "intervention,", "nous", "ne", "tiendrons",
    "pas", "plus", "de", "quelques", "minutes.", "Fin", "de", "transmission."
],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            },
            {
                "name": "Jeu de données caché 2",
                "data":  [
    "Citoyens", "de", "la", "galaxie,", "nous", "sommes", "rassemblés", "en",
    "ce", "jour", "historique", "pour", "proclamer", "l'instauration", "d'une",
    "nouvelle", "ère.", "Les", "traités", "de", "paix", "sont", "signés", "et",
    "toutes", "les", "hostilités", "prennent", "fin.", "Que", "cette", "union",
    "entre", "les", "mondes", "perdure", "et", "garantisse", "une", "prospérité",
    "durable", "pour", "tous."
],
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            }
        ],
        "contraintes": [
            {
                "name": "Pas de join",
                "validation": False,
                "message": "Vous avez utilisé la fonction join. L'exercice n'est pas validé",
                "impact": 20
            },
            {
                "name": "Trop de for",
                "validation": False,
                "message": "Vous avez utilisé trop de for. Vous perdez 1 point",
                "impact": 1
            }
        ],
        "bonus": [{
            "name": "Moins de 2 for",
            "validation": False,
            "message": "Vous avez réussi l'exercice avec moins de 2 for, +3 points !",
            "impact": 3
        }],
        "console": {
            "type": None,
            "message": []
        }
    }


    # ETAPE 2: Définition des jeux de données
    def input_function(input):
        ordre_attaque_conca = ""
        for k in range(len(input)):
            if k < len(input)-1:
                ordre_attaque_conca += input[k] + " "
            else:
                ordre_attaque_conca += input[k]
        return ordre_attaque_conca

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = input_function(jeu['data'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """
def concat(input):
    ordre_attaque_conca = ""
    for k in range(len(input)):
        if k < len(input)-1:
            ordre_attaque_conca += input[k] + " "
        else:
            ordre_attaque_conca += input[k]
    return ordre_attaque_conca
output = concat(input)

print(output)
"""

    append_log(f"Code utilisateur: {code_utilisateur}")

    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        # Contrainte de replace
        if contrainte['name'] == "Pas de join":
            if "join" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True

        # Contrainte trop de if
        if contrainte['name'] == "Trop de If":
            if code_utilisateur.count("if") > 1:
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
