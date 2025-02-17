"""
Lore :
Tony Stark, en travaillant sur des modèles mathématiques pour ses systèmes d'intelligence artificielle,
doit souvent résoudre des équations linéaires complexes. Le déterminant d'une matrice lui permet de déterminer
si un système d'équations a une solution unique, aucune solution, ou une infinité de solutions.

En comprenant le comportement des déterminants, Tony peut affiner les algorithmes de ses armures et prévoir
comment elles interagiront avec des environnements complexes ou imprévisibles, améliorant ainsi leur performance.

Enoncé:
Écrire un programme Python qui, à partir d'une matrice carrée de taille 2×2, calcule son déterminant.
le dertimant d'une

Interdit : numpy

Indices 1: La matrice doit contenir des valeurs flottantes
Indices 2: une matrice [[a , b],[c , d]] a pour determinant a*d - c*b
"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
matrice = [
    [2.0, 3.5],
    [1.0, 4.0]
]


# Résultat attendu :Déterminant de la matrice : 4.5



"""
Rédige un programme Python qui, à partir d'une matrice carrée de taille 2×2, calcule son déterminant.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau "matrice" et donnee le résultat: determinant
"""





#corection
def determinant(input):
    a = input[0][0]
    b = input[0][1]
    c =input[1][0]
    d = input[1][1]
    determinant = a * d - b * c
    return determinant


output=determinant(matrice)





