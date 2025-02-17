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

def execute_user_code(code, data, func_name): #code
    """
    Exécute le code utilisateur de manière sécurisée et renvoie le résultat ou une erreur.
    """
    local_namespace = {"enonce": data} #code
    restricted_globals = {}

    # Redirection de la sortie standard pour capturer la sortie du code utilisateur
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output


    try:
        exec(code, restricted_globals, local_namespace)
        exec_std_output = captured_output.getvalue()
        # Appeler la fonction utilisateur avec les paramètres fournis
        user_function = local_namespace.get(func_name)
        if user_function:
            resultat_utilisateur = user_function(local_namespace["enonce"])
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
                "name": "Phrase à inverser",
                "data": ".sonahT ertnoc tnettab es aciremA niatpaC te naM norI",
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact":15
            },
            {
                "name": "Jeu de données caché 1",
                "data": ".dragsA regétorp ruop uaetram nos esilitu rohT",
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact":3
            },
            {
                "name": "Jeu de données caché 2",
                "data": ".ardyH'l ed eémra'l ertnoc tnettab es eyekwaH te wodiW kcalB",
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": "",
                "impact":2
            }
        ],
        "contraintes":[
            {
                "name": "Pas de reversed",
                "validation": False,
                "message": "Vous avez utilisé la fonction reversed. L'exercice n'est pas validé",
                "impact":20
            },
            {
                "name": "Trop de for",
                "validation": False,
                "message": "Vous avez utilisé trop de for. Vous perdez 5 points",
                "impact":5
            },
            {
                "name": "Inversion par slicing",
                "validation": False,
                "message": "Vous n'avez pas utilisé le slicing pour inverser la chaîne. L'exercice n'est pas validé.",
                "impact": 10
            }
                        ],
        "bonus":[
    {
        "name": "Code optimisé",
        "validation": False,
        "message": "Votre code est optimisé et utilise peu de variables, +2 points !",
        "impact": 1
    },           
            ],
        "console":{
            "type":None,
            "message":[]
        }
                 }

    # ETAPE 2: Définition des jeux de données
    def reparo(texte):
        # Utilisation du slicing pour inverser la chaîne
        return texte[::-1]

    for jeu in resultat['jeux_de_donnees']:
        jeu['correction'] = reparo(jeu['data'])

    append_log(f"Jeux de données: {resultat['jeux_de_donnees']}")

    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(enonce):
        return enonce[::-1]"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.
    for contrainte in resultat['contraintes']:
        # Contrainte de replace
        if contrainte['name'] == "Pas de reversed":
            if "reverse" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
        
        # Contrainte trop de for
        if contrainte['name'] == "Trop de for":
            if code_utilisateur.count("for") > 1:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
                
        # Contrainte de Slicing
        if contrainte['name'] == "Inversion par slicing":
            if  "[::-1]" not in code_utilisateur:
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
        # Contrainte de replace
        if bonus['name'] == "Solution en une ligne":
            if code_utilisateur.count("\n") < 2:
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
