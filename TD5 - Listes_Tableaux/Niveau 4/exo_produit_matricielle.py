"""
Lore :
Dans l'atelier de Tony Stark, alors qu'il travaille sur des algorithmes complexes pour améliorer la performance de ses armures,
il se rend compte que le traitement des données matricielles est essentiel pour les calculs de simulation.
Pour créer des systèmes plus efficaces, il doit réaliser le produit de deux matrices.

Tony décide de relever ce défi en écrivant un programme Python. Conscient que l’utilisation de bibliothèques comme numpy
est interdite pour ce projet, il se plonge dans les mathématiques fondamentales de la multiplication des matrices.
Avec son esprit analytique, il construit un algorithme qui parcourt les éléments des deux matrices et calcule manuellement chaque valeur du produit.

Cette tâche, bien que technique, est cruciale pour ses projets. En maîtrisant la multiplication de matrices,
Tony s'assure que ses armures sont non seulement puissantes, mais également intelligentes, prêtes à faire face
aux défis de la bataille. Chaque calcul le rapproche un peu plus de son objectif de perfectionner la technologie de l'armure.

Énoncé :

Écrire un programme Python qui réalise le produit entre deux matrices de taille  𝑛×𝑛


Les deux matrices doivent être définies dans le programme et peuvent contenir des nombres entiers ou des flottants.
Le programme doit parcourir les éléments des matrices et effectuer le produit de manière manuelle, sans utiliser de bibliothèques comme numpy.

Indices : boucle imbriqué
Conditions :

L'algorithme doit être capable de multiplier des matrices de n'importe quelle taille nxn.
Affichez le résultat de la matrice produit.

"""

### Template fourni aux élèves

# Jeux de test
A = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [11, 13, 15, 17, 19],
    [21, 23, 25, 27, 29],
    [31, 33, 35, 37, 39]
]

# Définition de la deuxième matrice 5x5
B = [
    [5, 10, 15, 20, 25],
    [4, 8, 12, 16, 20],
    [3, 6, 9, 12, 15],
    [2, 4, 6, 8, 10],
    [1, 2, 3, 4, 5]
]
# Résultat attendu :[[70, 140, 210, 280, 350], [55, 110, 165, 220, 275], [205, 410, 615, 820, 1025], [355, 710, 1065, 1420, 1775], [505, 1010, 1515, 2020, 2525]]

#
"""
Rédige un programme Python qui réalise le produit entre deux matrices de taille  𝑛×𝑛

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées A et B et avoir pour résultat
 les variables: C 
"""


def produit_matricielle(input):
    A,B=input[0],input[1]

    lignes_A, colonnes_A = len(A), len(A[0])
    lignes_B, colonnes_B = len(B), len(B[0])
    C = []
    for i in range(lignes_A):
        ligne_resultat = []
        for j in range(colonnes_B):
            somme = 0
            for k in range(colonnes_A):
                somme += A[i][k] * B[k][j]
            ligne_resultat.append(somme)
        C.append(ligne_resultat)
    return C

output=produit_matricielle((A,B))
print(output)





