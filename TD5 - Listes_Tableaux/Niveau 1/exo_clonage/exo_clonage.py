"""
Lore :
Certains ingrédients pour potion sont très longs et fastidieux à préparer. Hermione a l'idée de les dupliquer à l'aide d'un sort.

Enoncé :
Créer un programme qui créé un NOUVEAU tableau à partir d'un tableau existant.
Puis remplacer l'élément d'indice 1 du tableau par "mandragore"

Indice 1 : faites des tests pour bien vous familiariser avec les tableaux. Visualiser l'effet de vos actions avec la fonction print (sur le nouveau et l'ancien tableau)
Indice 2 : si vous essayer de copier le tableau avec l'opérateur =, cela ne va pas créer un nouveau tableau mais une nouvelle attribution du même tableau.
Indice 3: utiliser la fonction copy ou encore le slicing pour créer un nouveau tableau à partir de l'ancien
"""


### Template fourni aux élèves

# Jeu de test
inventaire = ["sangsue", "plume", "poil de chat", "chenille", "rate de rat", "peau de serpent", "sang d'ogre"]


"""
Rédige un programme pour créer un nouveau tableau à partir d'un ancien

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser comme entrée inventaire et comme sortie nouvel_inventaire
"""


### Correction

## Version 1
nouvel_inventaire = inventaire.copy()
nouvel_inventaire[1] = "mandragore"

## Version 2
nouvel_inventaire = inventaire[:]
nouvel_inventaire[1] = "mandragore"
