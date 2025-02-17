"""
Lore :
Vous faites une partie d'échecs des Sorciers. Si vous déplacez votre fou, vous pouvez faire échec et mat.

Enoncé : 
En entrée est fourni l'échiquier qui est une matrice 8x8. L'objectif est de permuter un élement avec un autre dans la matrice.
Pour réaliser échec et mac, il faut déplacer le fou de la position D3 à la position A6.
Le résultat est le tableau echiquier après le déplacement du fou.

Indice 1: attention, l'indice d'un tableau commence par 0 en Python
Indice 2: pour une matrice, il faut d'abord renseigner l'indice de la ligne puis de la colonne. Par exemple, tab[3][5] correspond à la case de la 3e ligne et la 5e colonne.
Indice 3 : la position D3 correspond à la case de ligne n°5 et de colonne n°3. La position A6 correspond à la case de ligne n°2 et de colonne n°0.
Indice 4: pour faire une permutation, il est nécessaire d'utiliser une variable pour stocker temporairement une des valeurs à échanger.
"""

### Template fourni aux élèves

# Jeu de données
echiquier = [ 
 ['-', '-', 'R', 'T', '-', '-', '-', '-'],
 ['-', '-', '-', 'P', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', 'F', '-', '-'],
 ['-', '-', '-', 'F', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', 'R', '-', '-', '-', '_', '-']
]

# Résultat attendu :
echiquier = [ 
 ['-', '-', 'R', 'T', '-', '-', '-', '-'],
 ['-', '-', '-', 'P', '-', '-', '-', '-'],
 ['F', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', 'F', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', 'R', '-', '-', '-', '_', '-']
]

"""
Rédige un programme pour réaliser une permutation et modéliser le déplacement du fou

/!\ Le résultat attendu doit être contenu dans la variable échiquier (pour que le code soit correctement testé)
"""

### Correction

tmp = echiquier[5][3]
echiquier[5][3] = echiquier[2][0]
echiquier[2][0] = tmp

