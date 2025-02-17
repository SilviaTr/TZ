
"""
Lore :
New York est sous la menace d’un virus informatique libéré par OsCorp, perturbant les systèmes de défense de la ville.
Sans ses outils habituels comme Numpy, Spider-Man, alias Peter Parker, doit user de son génie scientifique pour résoudre un problème critique.
Sa mission : écrire un programme réalisant le produit entre un vecteur ligne et un vecteur colonne de même longueur.
Utiliser vos connaissances, Spidey n'a pas droit à l'erreur.

Enoncé:

Écrire un programme Python qui realise un produit entre un vecteur ligne et colone de meme longueur.

Interdit : numpy

Indices 1: Une boucle for ou while peuvent être envisagée.
Indices 2: initialiser une somme a zero

"""

### Template fourni aux élèves

# Jeux de test


# Liste initiale
list_1 = [31.29, 11.3, 85.39, 65.46, 2.78, 35.34, 8.91, 81.53, 87.75, 41.39, 59.09, 7.61, 5.04, 92.14, 16.94]

list_2 = [95.45, 85.83, 8.1, 71.83, 91.56, 91.93, 22.95, 45.37, 65.15, 90.09, 53.02, 74.74, 50.04, 49.89, 62.39]


# Résultat attendu :35810.4175

"""
Rédige un programme Python qui realise un produit entre un vecteur ligne et colone de meme longueur.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableaux d'entrée list_1 et list_2 et avoir pour résultat
 les variables: produit_scalaire
"""
### Correction


def produit_scalaire(input):
    p_s = 0
    for i in range(len(input[0])):
        p_s += input[0][i] * input[1][i]
    return p_s
output = produit_scalaire((list_1,list_2 ))
print(output)





