
"""
Lore :
Dans sa quête de domination mondiale, Ultron a décidé de concevoir une matrice de données qui contiendrait des informations stratégiques.
Cette matrice, de taille 5x5, doit être remplie d'entiers allant de 1 à 25, organisés ligne par ligne.
Cependant, Ultron a une règle stricte : il ne doit pas utiliser de bibliothèques externes comme NumPy pour construire cette matrice.
Pour mener à bien cette tâche, il devra faire preuve de méthode et de rigueur, utilisant des boucles et des listes pour structurer ses données efficacement.


Enoncé:
Écrire un programme Python qui crée une matrice de taille 5x5 où les termes sont les entiers de 1 à 25, organisés par ligne.

Interdit : numpy

Indices 1: Crée une boucle pour parcourir pour creer les elements de la liste.
Indices 2: Utilise une liste tampon pour stocker les éléments de chaque ligne.
Indices 3: Utilise Append()


"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
#None


# Résultat attendu :
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]




"""
Rédige un programme Python qui crée une matrice de taille 5x5 où les termes sont les entiers de 1 à 25, organisés par ligne.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser donnee le résultat: matrice
"""


### Correction
def marice_crea():
    matrice = []
    for i in range(5):
        ligne = []
        for j in range(5):
            ligne.append(i * 5 + j + 1)
        matrice.append(ligne)
    return matrice

output=marice_crea()
