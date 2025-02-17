
"""
Lore :

Dans le laboratoire de Tony Stark, le bruit des machines et des circuits s'entremêle à l'odeur du métal chaud.
Alors qu'il se prépare à affronter une nouvelle menace, il réalise qu'il doit faire l'inventaire de ses armures.
Chaque modèle, une prouesse d'ingénierie, est catalogué avec son nom et sa capacité en millions de dollars.

Conscient que certaines armures ne répondent plus à ses normes, il décide de retirer celles dont la capacité est
inférieure à 100 millions ou supérieure à 200 millions. Pour ce faire, Tony se met à coder un programme Python.
Son objectif est de calculer la somme des capacités des armures, déterminant ainsi son arsenal prêt au combat.

Chaque ligne de code résonne comme une promesse : seules les armures dignes de son nom survivront à ce tri.
Dans cette quête pour l'excellence, Tony sait que seul le meilleur peut défendre l'humanité.

Enoncé:

Écrire un programme Python qui fait la somme de toute les armures de tony et qui retire celle qui sont inferieur a 100 m et superieur a 200,
dans le tuple les nombre sont en million.

Interdit : numpy

Indices 1: Une boucle for ou while peuvent être envisagée.
Indices 2: initialiser une somme a zero
Indices 3: utilise remove()

"""

### Template fourni aux élèves

# Jeux de test


# Liste initiale
armors = [
    ('Mark I', 25),
    ('Mark II', 50),
    ('Mark III', 100),
    ('Mark IV', 120),
    ('Mark V', 90),
    ('Mark VI', 150),
    ('Mark VII', 180),
    ('Mark XLII', 210),
    ('Mark L', 250),
    ('Mark LXXXV', 300),
    ('Hulkbuster (Mark XLIV)', 350),
    ('Rescue', 210)
]

# Résultat attendu :Sum: 2035
#[('Mark III', 100), ('Mark IV', 120), ('Mark VI', 150), ('Mark VII', 180)]


"""
Rédige un programme Python qui fait la somme de toute les armures de tony et qui retire celle qui sont inferieur a 100 m et superieur a 200,
dans le tuple les nombre sont en million.
/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée armors et avoir pour résultat
 les variables: somme
"""

# Initialize the total sum
def armure(input):
    somme = 0
    for i in input[:]:
        somme += i[1]
        if i[1] < 100 or i[1]>200:
            input.remove(i)
    return somme

output = armure(armors)

print(output)

