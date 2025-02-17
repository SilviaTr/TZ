import json
import random
import copy
import re
import traceback
import sys
import io
import os
from math import ceil

def append_log(message):
    global log_messages
    log_messages += message + "\n"

def execute_user_code(code, data, func_name):
    """
    Exécute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    
    local_namespace = {
        "quantité_originale": data["quantité_originale"],
        "nb_dose": data["nb_dose"]
    } 
    restricted_globals = {"ceil": ceil}

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
            resultat_utilisateur = user_function(local_namespace["quantité_originale"], local_namespace["nb_dose"])  # Passer les bonnes variables
  # Passer la liste
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
                "name": "Nombre Conversion",
                "data": {"quantité_originale":[2,4,9],
                         "nb_dose":3},
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 15
            },
            {
                "name": "Jeu de données caché 1",
                "data": {"quantité_originale":[0,0,0],
                         "nb_dose":3},
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 3
            },
            {
                "name": "Jeu de données caché 2",
                "data": {"quantité_originale":[2,4,9],
                         "nb_dose":0},
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact": 2
            }
        ],
        "contraintes":[

            {
                "name": "Utilisation de ceil pour arrondir",
                "validation": False,
                "message": "Vous devez utiliser la fonction 'ceil' pour arrondir la valeur au chiffre supérieur.",
                "impact": 20
            },
            {
                "name": "Nombre entier",
                "validation": False,
                "message": "Le résultat doit être un entier.",
                "impact": 10
            }
        ],
        "bonus":[
            {
                "name": "Entrée valide",
                "validation": False,
                "message": "Vous avez validé l'entrée (ex. : un nombre positif), +5 points !",
                "impact": 5
            }],
        "console":{
            "type":None,
            "message":[]
        }
    }

    # ETAPE 2: Définition des jeux de données
    def reparo(quantite_originale, nb_dose):

        solution = []
        for quantite in quantite_originale:
            solution.append(ceil(quantite * nb_dose * 6))  # Conversion en petites cuillères
        return solution

    for jeu in resultat['jeux_de_donnees']:
        quantite_originale = jeu['data']['quantité_originale']
        nb_dose = jeu['data']['nb_dose']
        jeu['correction'] = reparo(quantite_originale, nb_dose)

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """from math import ceil
def reparo(quantite_originale, nb_dose):
    solution = []
    for quantite in quantite_originale:  # L'indentation doit être uniforme
        solution.append(ceil(quantite * nb_dose * 6))  # Conversion en petites cuillères
    return solution"""
    
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:

        # Contrainte "Utilisation de ceil pour arrondir"
        if contrainte['name'] == "Utilisation de ceil pour arrondir":
            if "ceil" not in code_utilisateur:
                contrainte['validation'] = False  # Si 'ceil' n'est pas utilisé, la contrainte échoue
            else:
                contrainte['validation'] = True  # Si 'ceil' est utilisé, la contrainte est validée

        # Contrainte "Nombre entier"
        if contrainte['name'] == "Nombre entier":
            if "int(" in code_utilisateur or "ceil" in code_utilisateur:
                contrainte['validation'] = True  # Le résultat doit être un entier
            else:
                contrainte['validation'] = False  # Si ce n'est pas un entier, la contrainte échoue
        
        if contrainte['validation'] == False:
            append_log("Contrainte non respectée: "+contrainte['name'])
            resultat['note'] = resultat['note'] - contrainte['impact']
            resultat['note'] = 0 if (resultat['note'] < 0) else resultat['note']
        else:
            append_log(f"Contrainte respectée: {contrainte}")
    
    # ETAPE 4: Définition des bonus de l'exercice.
    for bonus in resultat['bonus']:
        
        # Bonus "Entrée valide"
        if bonus['name'] == "Entrée valide":
            if 'float' in code_utilisateur or 'int' in code_utilisateur:
                bonus['validation'] = True  # L'entrée est valide si 'float' ou 'int' sont utilisés
            else:
                bonus['validation'] = False
        
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
