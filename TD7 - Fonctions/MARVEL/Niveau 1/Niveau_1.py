"""
Lore :
Pour créer la nouvelle armure Mark XLVI, Tony Stark doit vérifier qu'il a bien tous les composants nécessaires pour l'assembler. 
Vous souhaitez l'aider en vérifiant que les composants listés pour l'armure sont bien présents dans son atelier.

Enoncé :
La fonction renvoie un booléen.
Écrire une fonction `armure_realisable(armure, atelier)` permettant de tester si tous les composants du tableau armure sont aussi présents dans le tableau atelier.
On supposera que les composants sont des chaînes de caractères et que les éléments d'armure sont tous distincts.

Indice 1 : Vous avez déjà réalisé un exercice similaire dans le chapitre sur les listes. Vous pouvez maintenant clarifier votre code en utilisant une boucle simple pour tester la présence de chaque composant dans l'atelier.
Indice 2 : Pour chaque composant de l'armure, vérifiez qu'il est bien présent dans l'atelier avant de passer au suivant. Utilisez une boucle pour cela.
Indice 3 : Si un composant est absent de l'atelier, la fonction doit retourner `False` immédiatement, sans vérifier les autres composants.
"""

### Template fourni aux élèves

# Jeux de test
armure = ["réacteur arc", "alliage Vibranium", "nano-capteurs", "moteur Stark", "plaques titane"]

atelier1 = [
    "réacteur arc",
    "plaque en carbone",
    "alliage Vibranium",
    "gants en vibranium",
    "nano-capteurs",
    "moteur Stark",
    "plaques titane",
    "micro-réacteurs",
    "armature en acier",
]

# Résultat attendu : armure_realisable(armure, atelier1) = True

atelier2 = [
    "réacteur arc",
    "plaque en carbone",
    "moteur d'hélicoptère",
    "panneau solaire",
    "carburant haute densité",
    "alliage Vibranium",
    "filaments en acier",
]
# Résultat attendu : armure_realisable(armure, atelier2) = False






def armure_realisable(armure, atelier):
    armure_faisable = True
    "cette fonction renvoie un booléen"
    return armure_faisable

### Correction


def armure_realisable(armure, atelier):
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
    
    return armure_faisable
