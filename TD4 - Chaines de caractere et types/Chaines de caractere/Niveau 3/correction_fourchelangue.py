import json
import random
import copy
import re
import traceback
import sys
import io
import os

def sanitize_user_code(code):
    # Liste des motifs interdits et leur remplacement sécurisé (None signifie suppression)
    blacklist = [
        (r'\bexec\b', ''),  # Supprime `exec`
        (r'\beval\b', ''),  # Supprime `eval`
        (r'\bopen\b', ''),  # Supprime `open`
        (r'\bsubprocess\b', ''),  # Supprime `subprocess`
        (r'__import__', ''),  # Supprime `__import__`
        (r'getattr\s*\(', ''),  # Supprime les appels à `getattr()`
        (r'(os|sys|subprocess|shlex)\.', ''),  # Supprime l'accès aux modules dangereux
    ]

    for pattern, replacement in blacklist:
        if replacement is None:
            code = re.sub(pattern, '', code)  # Supprime le motif
        else:
            code = re.sub(pattern, replacement, code)  # Remplace le motif

    return code

if __name__ == "__main__":
    output_name = "REPLACE_ME_OUTPUT_NAME"
    log_folder = "output"

    log_messages = ""

    def append_log(message):
        global log_messages
        log_messages += message + "\n"

    files_to_delete = [
        os.path.join(log_folder, f"{output_name}_erreur.json"),
        os.path.join(log_folder, f"{output_name}_resultats.json"),
        os.path.join(log_folder, f"{output_name}_logs.txt"),
        f"{output_name}.py_output.txt"
    ]

    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            append_log(f"Fichier précédent supprimé: {file}")
        else:
            append_log(f"Aucun fichier précédent à supprimer: {file}")

    append_log(f"Nom de la variable de sortie: {output_name}")

    # Configuration des logs
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"{output_name}_logs.txt")
    append_log("Démarrage de l'exercice")
    # ETAPE 1: Définition des jeux de données

    # Jeu de données visible par l'utilisateur
    jeu_de_donnee_visible = {"name": "Jeu de données visible", "data": "y'fpmfpdn dfn nflhfpmn bekkqpxjqfl csfb kex" ,"alphabet" : "abcdefghijklmnopqrstuvwxyz"," alphabet_fourchelangue " : "cabdfgizxyvokpehjlnmqstrwu", "impact": 3 }

    
    append_log(f"Jeu de données visible: {jeu_de_donnee_visible}")

    # Jeu de données caché
    # Option 1: Utilisation de jeu de données prédéfinis
    dataset1 = {"name": "Jeu de test caché 1", "data": "Jns cabpvlikj hlnhqykj jn Zpjxx",  "alphabet" : "abcdefghijklmnopqrstuvwxyz",\
                            "alphabet_fourchelangue" : "cabdfgizxyvokpehjlnmqstrwu", "impact": 3}
    dataset2 = {"name": "Jeu de test caché 2", "data": "Mhawlq vrjg jns xjhnnljq du j'hjmhmj",  "alphabet" : "abcdefghijklmnopqrstuvwxyz",\
                            "alphabet_fourchelangue" : "cabdfgizxyvokpehjlnmqstrwu", "impact": 3}
    append_log(f"Jeu de données cachées: {[dataset1, dataset2]}")

    jeu_de_donnees = [dataset1, dataset2, jeu_de_donnee_visible]

    # Le code utilisateur est injecté ici
    code_utilisateur = """REPLACE_ME_CODE_UTILISATEUR"""
    append_log(f"Code utilisateur: {code_utilisateur}")
    # Étape 2 (Optionnel): Définition des contraintes de l'exercice.
    # On n'a pas le droit à la fonction replace

    contrainte = True  # Par défaut, on considère que la contrainte est respectée
    contraintesMessages = []  # Liste des messages d'erreur pour les contraintes
    contraintesHard = []  # Liste des contraintes non respectées
    # Vérification des contraintes

    if "replace" in code_utilisateur:
        contrainte = False
        contraintesMessages.append("Vous avez utilisé la fonction replace.")
        contraintesHard.append("Vous avez utilisé la fonction replace.")
        append_log("Contrainte non respectée: fonction replace utilisée")

    
    condition1 = False
    if code_utilisateur.count("if") > 1:
        condition1 = True
        contraintesMessages.append("Attention une solution utilisant moins de if est possible, votre code est correct mais vous n'obtiendrez pas l'ensemble des points.")
        append_log("Points en moins: trop de if")

    condition3 = False
    if code_utilisateur.count("for") > 1:
        condition3 = True
        contraintesMessages.append("Attention une solution utilisant moins de for est possible, votre code est correct mais vous n'obtiendrez pas l'ensemble des points.")
        append_log("Points en moins: trop de for")

    condition4 = False
    if code_utilisateur.count("while") > 1:
        condition4 = True
        contraintesMessages.append("Attention une solution utilisant moins de while est possible, votre code est correct mais vous n'obtiendrez pas l'ensemble des points.")
        append_log("Points en moins: trop de while")


    append_log(f"Contrainte respectée: {contrainte}")
    append_log(f"Messages de contraintes: {contraintesMessages}")
    # ETAPE 3: Définition des contraintes système (éviter les hacks, les boucles infinies, etc.)

    # Sanitisation du code utilisateur
    # Remplacement des mots interdits / Suppression des tentatives de hack
    code_utilisateur_sanitize = sanitize_user_code(code_utilisateur)
    append_log(f"Code utilisateur après sanitisation: {code_utilisateur_sanitize}")
    # ETAPE 4: Fonction de test
   
    def reparo(phrase,alphabet_fourchelangue, alphabet ):
        phrase_traduite=""
        for i in range(len(phrase)):
            if phrase[i] in alphabet_fourchelangue:
                 j = 0
                 while phrase[i] != alphabet_fourchelangue[j]: # pour trouver l'indice de la lettre dans l'alphabet fourchelangue
                     j+=1

                 phrase_traduite = phrase_traduite + alphabet[j] # a partir de l'indice j, on récupère la lettre correspondante en français
            else:
                 phrase_traduite += phrase[i]
        return phrase_traduite


    append_log(f"Fonction de test définie: {reparo}")
    # Exécution et validation du code utilisateur
    try:
        validation_output = []
        contrainte_longueur = False
        user_output = ""
        for dataset_index, dataset in enumerate(jeu_de_donnees):
            append_log(f"Exécution du code utilisateur pour le jeu de données {dataset['name']}")

            # ETAPE 5: Exécution du code utilisateur
            input_data = copy.deepcopy(dataset["data"])
            append_log(f"Entrée du code utilisateur: {input_data}")

            # Execution du code utilisateur avec un espace de nommage sécurisé
            local_namespace = {"input": input_data}
            restricted_globals = {}

            original_stdout = sys.stdout
            captured_output = io.StringIO()
            sys.stdout = captured_output
            
            try:
                exec(code_utilisateur_sanitize, restricted_globals, local_namespace)
                exec_std_output = captured_output.getvalue()
                if exec_std_output:
                    user_output += "Output execution " + dataset["name"] + ": \n"
                    user_output += exec_std_output
                resultat_utilisateur = local_namespace.get("output")
                append_log(f"Résultat du code utilisateur: {resultat_utilisateur}")

                if not contrainte_longueur:
                    texte_initial = dataset["data"]
                    texte_apres_reparo = resultat_utilisateur
                    append_log(f"Texte initial: {texte_initial}")
                    append_log(f"Texte après réparo: {texte_apres_reparo}")
                    if type(texte_initial) == str and type(texte_apres_reparo) == str and len(texte_apres_reparo) != len(texte_initial):
                        contrainte = False
                        contraintesMessages.append("Le texte après l'application de la fonction n'a pas la bonne longueur, l'ensemble du texte n'a pas été réparé.\nVérifier que vous parcourez bien l’ensemble du texte à déchiffrer, que se passerait-il si le remplacement devait avoir lieu à la fin du texte ?")
                        contraintesHard.append("Le texte après l'application de la fonction n'a pas la bonne longueur, l'ensemble du texte n'a pas été réparé.")
                        append_log(f"Contrainte non respectée: l'ensemble du texte n'a pas été réparé/\n Longueur du texte utilisateur: {len(texte_apres_reparo)}\n Longueur du texte initial: {len(texte_initial)}")
                        contrainte_longueur = True
                
                append_log(f"Sortie standard du code utilisateur: {user_output}")
            except Exception as e:
                raise e
            finally:
                sys.stdout = original_stdout

            

            # ETAPE 6: Validation du code utilisateur
            correction = reparo(dataset["data"])
            validation_output.append({
                "name": dataset['name'],
                "validation": resultat_utilisateur == correction,
                "resultat_utilisateur": resultat_utilisateur,
                "correction": correction,
                "impact": dataset["impact"]
            })
            append_log(f"Validation pour le jeu de données {dataset['name']}: {validation_output[-1]}")

        append_log(f"Résultat global de la validation: {validation_output}")
        # NOUVELLE ETAPE:

        # Ici on va attribuer une note en fonction de divers conditions, la note sera un str au format "X/Y"
        # ex: 4/7
        # None = Pas de note
        # La note est pondérée sur 20 points.
        # Condition 1 : un seul if est utilisé sinon chaque test validé ne vaut que 0.75 point

        note = {"note": sum([test['impact'] for test in validation_output if test["validation"]]) / sum([dataset['impact'] for dataset in jeu_de_donnees]) * 20 , 
                "modificateurs": [],
                "note_finale": sum([test['impact'] for test in validation_output if test["validation"]]) / sum([dataset['impact'] for dataset in jeu_de_donnees]) * 20}

        append_log(f"Note de base: {note['note']}")
        # SOFT CONTRAINTES

        if code_utilisateur.count("if") > 1:
            note_avec_modificateur = sum([test['impact'] * 0.75 for test in validation_output if test["validation"]]) / sum([dataset['impact'] for dataset in jeu_de_donnees]) * 20
            append_log(f"Points en moins: trop de if\nNote avec modificateur: {note_avec_modificateur}")
            # Si + de 1 if, chaque test validé ne vaut que 75%. La valeur du modificateur est la différence entre la note actuelle et la note avec le modificateur
            note["modificateurs"].append({"Nom": "Trop de if", "Valeur": note_avec_modificateur - note["note"]  , "Description": "Vous avez utilisé trop de if, chaque test validé ne vaut que 75%."})

        if code_utilisateur.count("[]") >= 1:
            note_avec_modificateur = sum([test['impact'] * 0.75 for test in validation_output if test["validation"]]) / sum([dataset['impact'] for dataset in jeu_de_donnees]) * 20
            append_log(f"Points en moins: tableau utilisé\nNote avec modificateur: {note_avec_modificateur}")
            note["modificateurs"].append({"Nom": "Tableau utilisé", "Valeur": note_avec_modificateur - note["note"]  , "Description": "Vous avez utilisé un tableau, chaque test validé ne vaut que 75%."})
        
        if code_utilisateur.count("for") > 1:
            note_avec_modificateur = sum([test['impact'] * 0.75 for test in validation_output if test["validation"]]) / sum([dataset['impact'] for dataset in jeu_de_donnees]) * 20
            append_log(f"Points en moins: trop de for\nNote avec modificateur: {note_avec_modificateur}")
            # Si + de 1 for, chaque test validé ne vaut que 75%. La valeur du modificateur est la différence entre la note actuelle et la note avec le modificateur
            note["modificateurs"].append({"Nom": "Trop de for", "Valeur": note_avec_modificateur - note["note"]  , "Description": "Vous avez utilisé trop de for, chaque test validé ne vaut que 75%."})

        # la note finale est la note de base moins la somme des modificateurs
        note["note_finale"] = note["note"] + sum([modificateur["Valeur"] for modificateur in note["modificateurs"]])

        if not contrainte:
            note["note_finale"] = 0
            note["note"] = 0
            note["modificateurs"].append({"Nom": "Contrainte non respectée", "Valeur": 0, "Description": "Vous avez enfreint une ou plusieurs contraintes: note nulle -\n" + "\n".join(contraintesHard)})
            append_log("Contrainte non respectée: note nulle")

        append_log(f"Note attribuée: {note['note_finale']}")
        # ETAPE 7: Ecriture des résultats dans un fichier au format JSON
        resultats_file = os.path.join(log_folder, f"{output_name}_resultats.json")
        with open(resultats_file, "w") as file:
            json.dump({
                "validation_output": validation_output,
                "contrainte": contrainte,
                "contraintesMessages": contraintesMessages,
                "defis": None,
                "user_output": user_output,
                "note": note,
                "success": contrainte and all(test["validation"] for test in validation_output)
            }, file, indent=4)
            append_log(f"Résultats écrits dans le fichier: {resultats_file}")

    except Exception as e:
        error_info = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        append_log(f"Erreur lors de l'exécution de l'exercice: {error_info}")
        # En cas d'erreur, on écrit l'erreur et des informations supplémentaires dans un fichier
        erreur_file = os.path.join(log_folder, f"{output_name}_erreur.json")
        with open(erreur_file, "w") as file:
            json.dump(error_info, file, indent=4)
            append_log(f"Informations d'erreur écrites dans le fichier: {erreur_file}")

    append_log("Fin de l'exercice")

    with open(log_file, "w") as f:
        f.write(log_messages)
