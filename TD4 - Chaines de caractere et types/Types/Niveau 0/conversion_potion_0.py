"""
Lore :

Le professeur Rogue a demandé à Rohn de travailler à la confection d'une potion donnant le pouvoir de faire taire quiconque aurait le malheur de la boire. 
Rohn a besoin de ton aide : il a horreur des conversions, et tout est indiqué en louche alors qu'il n'a à sa disposition qu'une petite cuillère !
Une louche contient l'équivalent de 6 petites cuillères. 

La recette indique :

Pour 1 fiole de potion silencieuse :
-	2 louches de sève d'harmonie
-	½ louche d'élixir de quiétude
-	¼ louche de nectar de tranquillité

Rohn doit convertir ces quantités en cuillères, une étape cruciale pour réussir la potion. 
Heureusement tu proposes de créer un sort « le silencio » pour l'aider à réaliser sa potion.

Niveau 0 :
Écris un programme qui renvoie la quantité nécessaire de nectar de tranquillité en nombre de petites cuillères (ce nombre peut être décimal).
"""
import random

# jeu de données visible par l'utilisateur

nombre = 0.25

# jeu de test caché

nombre1, nombre2, nombre3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

# Correction
solution = nombre * 6

""" Préparation avec template pour le nouveau site """
"""
import json
import random
import copy
import re
import traceback

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
    # ETAPE 1: Définition des jeux de données

    # Jeu de données visible par l'utilisateur
    jeu_de_donnee_visible = [0.25]

    # Jeu de données caché
    # Choix de 3 jeux de données aléatoires d'éléments entre 1 et 100
    jeu_de_donnees = [random.sample(range(1, 100)) for _ in range(3)]

    # On récupère le code utilisateur depuis un fichier
    with open("exercice1_user1.txt", "r") as file:
        code_utilisateur = file.read()

    # Étape 2 (Optionnel): Définition des contraintes de l'exercice.
    # Exemple: On ne peut utiliser au maximum que 1 boucle for

    contrainte = True  # Par défaut, on considère que la contrainte est respectée
    contraintesMessages = []  # Liste des messages d'erreur pour les contraintes
    # Vérification des contraintes (exemple simplifié)
    if code_utilisateur.count("for") > 1:
        contrainte = False
        contraintesMessages.append("Vous avez utilisé plus d'une boucle for.")

    # ETAPE 3: Définition des contraintes système (éviter les hacks, les boucles infinies, etc.)

    # Sanitisation du code utilisateur
    # Remplacement des mots interdits / Suppression des tentatives de hack
    code_utilisateur = sanitize_user_code(code_utilisateur)
    # Trouver la liste des mots interdits/à remplacer


    # Tout ce qui est en dessous est du "work in progress" et n'est pas encore fonctionnel

    # Exécution et validation du code utilisateur
    try:
        validation_output = []
        for dataset, index in enumerate(jeu_de_donnees):

            # ETAPE 4: Exécution du code utilisateur

            input = copy.deepcopy(dataset)

            # Execution du code utilisateur avec un espace de nommage sécurisé et la commande "exec"
            local_namespace = {"input": input}
            restricted_globals = {}

            exec(code_utilisateur, restricted_globals, local_namespace)

            resultat_utilisateur = local_namespace.get("output")

            # ETAPE 5: Validation du code utilisateur

            correction = dataset * 6
            validation_output.append({
                "validation": resultat_utilisateur == correction,
                "resultat_utilisateur": resultat_utilisateur,
                "correction": correction
            })

        # ETAPE 6: Gestion des défis
        # Gestion de trophées
        # Défi: Ne pas utiliser de boucle for/while. Solution: utiliser la fonction "sum()".

        defis = []
        if code_utilisateur.count("for") < 1 and code_utilisateur.count("while") < 1:
            defis.append("Défi: Ne pas utiliser de boucle for/while. Solution: utiliser la fonction 'sum()'.")

        # ETAPE 7: Ecriture des résultats dans un fichier au format JSON
        with open("exercice1_user1_resultats.txt", "w") as file:
            file.write(json.dumps({
                "validation_output": validation_output,
                "contrainte": contrainte,
                "contraintesMessages": contraintesMessages,
                "defis": defis
            }))

    except Exception as e:
        error_info = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        # En cas d'erreur, on écrit l'erreur et des informations supplémentaires dans un fichier
        with open("exercice1_user1_erreur.txt", "w") as file:
            file.write(json.dumps(error_info, indent=4))
"""