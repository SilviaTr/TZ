"""
Lore :
Pour l'examen du cours de Potions, il faut réaliser une potion de ratatinage. Pour cela, vous
souhaitez vérifier que vous avez bien tous les ingrédients nécessaires pour la recette.

Enoncé :
Écrire une fonction contient(sac, ingredient) permettant de tester si un ingrédient est inclus dans le tableau sac. La fonction renvoie un booléen.
Écrire une fonction potion_realisable(recette, sac) permettant de tester si tous les ingrédients du tableau recette sont aussi présents dans le tableau sac.
On supposera que les ingrédients sont des chaines de caractères et que les éléments de recette sont tous distincts.


Indice 1 : vous avez déjà réalisé un exercice similaire dans le chapitre sur les listes. Vous pouvez maintenant clarifier
votre code en utilisant la fonction intermédiaire appartient.
Indice 2 : la fonction potion_realisable appelle la fonction contient
Indice 3 : pour chaque ingrédient de la recette, vérifier que le sac contient bien l'ingrédient.
"""

### Template fourni aux élèves

# Jeux de test
recette = ["chenille", "jus de figue", "rate de rat", "poudre jaune", "sangsue"]

sac1 = [
    "sangsue",
    "peau de serpent",
    "jus de figue",
    "poil de chat",
    "rate de rat",
    "mandragore",
    "poudre jaune",
    "chenille",
    "bave d'ogre",
]

# Résultat attendu : potion_realisable(recette, sac1) = True

sac2 = [
    "sangsue",
    "peau de serpent",
    "aile de chauve-souris",
    "ecorce de saule cogneur",
    "sang de dragon",
    "chenille",
    "plume",
]
# Résultat attendu : potion_realisable(recette, sac2) = False

"""
Complète les deux fonctions en conservant leur signature
"""


def contient(sac, ingredient):
    "cette fonction renvoie un booléen"


def potion_realisable(recette, sac):
    "cette fonction renvoie un booléen"


### Correction


def contient(sac, ingredient):
    ingredient_dans_sac = False
    indice_sac = 0
    while indice_sac < len(sac) and not ingredient_dans_sac:
        if sac[indice_sac] == ingredient:
            ingredient_dans_sac = True
        indice_sac += 1
    return ingredient_dans_sac


def potion_realisable(recette, sac):
    recette_faisable = True
    indice_recette = 0
    while indice_recette < len(recette) and recette_faisable:
        if not contient(sac, recette[indice_recette]):
            recette_faisable = False
        indice_recette += 1
    return recette_faisable
