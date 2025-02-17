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
        "armure": data["armure"],
        "atelier": data["atelier"]
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
            resultat_utilisateur = user_function(local_namespace["armure"], local_namespace["atelier"])  # Passer les bonnes variables
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
        "success":False,
        "note":20,
        "jeux_de_donnees":[ 
        {
                "name": "Armure complète",
                "data": {
                    "armure": ["réacteur arc", "alliage Vibranium", "nano-capteurs", "moteur Stark", "plaques titane"],
                    "atelier": [
                        "réacteur arc",
                        "plaque en carbone",
                        "alliage Vibranium",
                        "gants en vibranium",
                        "nano-capteurs",
                        "moteur Stark",
                        "plaques titane",
                        "micro-réacteurs",
                        "armature en acier"
                    ]
                },
                "hidden": False,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": True,
                "impact": 15
            },
            {
                "name": "Jeu de données caché 1",
                "data": {
                    "armure": ["réacteur arc", "alliage Vibranium", "nano-capteurs", "moteur Stark", "plaques titane"],
                    "atelier": [
                        "réacteur arc",
                        "plaque en carbone",
                        "moteur d'hélicoptère",
                        "panneau solaire",
                        "carburant haute densité",
                        "alliage Vibranium",
                        "filaments en acier"
                    ]
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": False,
                "impact": 2
            },
            {
                "name": "Jeu de données caché 2",
                "data": {
                    "armure": ["réacteur arc", "alliage Vibranium", "nano-capteurs", "moteur Stark", "plaques titane", "système de navigation", "blaster intégré"],
                    "atelier": [
                        "réacteur arc",
                        "plaque en carbone",
                        "nano-capteurs",
                        "moteur Stark",
                        "plaques titane",
                        "système de navigation",
                        "blaster intégré",
                        "gants en vibranium",
                        "armature en acier"
                    ]
                },
                "hidden": True,
                "validation": False,
                "resultat_utilisateur": "",
                "correction": False,
                "impact": 3
            }
        ],
        "contraintes": [
            {
                "name": "Limiter l'utilisation des fonctions externes",
                "validation": False,
                "message": "Vous ne devez pas utiliser des fonctions externes telles que 'join()', 'map()', ou 'filter()'. L'objectif est de recourir uniquement à une simple boucle.",                "impact": 10
            },
            {
                "name": "Pas d'utilisation de in",
                "validation": False,
                "message": "L'utilisation de l'opérateur 'in' est interdite. Vous devez vérifier la présence des composants en utilisant une autre méthode, comme une boucle 'for'.",
                "impact": 5
            },
            {
                "name": "Pas d'utilisation de any() ou all()",
                "validation": False,
                "message": "Vous ne devez pas utiliser les fonctions 'any()' ou 'all()' pour vérifier la présence des composants. Utilisez une boucle 'for' simple à la place.",
                "impact": 5
            }
        ],
        "console":{
            "type":None,
            "message":[]
        }
    }



    # Le code utilisateur est injecté ici
    code_utilisateur = """def reparo(armure, atelier):
    armure_faisable = True
    indice_armure = 0
    
    while indice_armure < len(armure) and armure_faisable:
        composant = armure[indice_armure]
        composant_dans_atelier = False
        indice_atelier = 0
        while indice_atelier < len(atelier) and not composant_dans_atelier:
            if atelier[indice_atelier] == composant:
                composant_dans_atelier = True
            indice_atelier += 1
        
        if not composant_dans_atelier:
            armure_faisable = False
        
        indice_armure += 1
    
    return armure_faisable"""
    
    append_log(f"Code utilisateur: {code_utilisateur}")
    
    # Étape 3: Définition des contraintes de l'exercice.
   
    for contrainte in resultat['contraintes']:
        
        # Contrainte : Pas de in
        if contrainte['name'] == "Pas d'utilisation de in":
            if " in " in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True
  
        # Contrainte : Limiter l'utilisation des fonctions externes comme join, map, filter
        if contrainte['name'] == "Limiter l'utilisation des fonctions externes":
            if "join" in code_utilisateur or "map" in code_utilisateur or "filter" in code_utilisateur:
                contrainte['validation'] = False
            else:
                contrainte['validation'] = True             
    
        # Contrainte : Pas d'utilisation de 'any()' ou 'all()'
        if contrainte['name'] == "Pas d'utilisation de any() ou all()":
            if "any(" in code_utilisateur or "all(" in code_utilisateur:
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
