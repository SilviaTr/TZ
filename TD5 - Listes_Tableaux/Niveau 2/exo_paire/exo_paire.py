"""
Lore :
Tony Stark, se retrouve confronté à une liste de données hétérogènes.
Parmi ces éléments, certains sont des nombres impairs qui ne sont pas pertinents pour son analyse actuelle.
Afin de filtrer ces informations et de ne garder que les éléments pairs, il doit concevoir un programme efficace.
Avec son génie, Tony sait qu'il peut procéder sans outils sophistiqués, simplement en utilisant une boucle pour parcourir la liste et éliminer les nombres indésirables.

Enoncé:

Écrire un programme Python qui retire tout les elements impaire d'une liste.
Interdit : remove()

Indices 1: Crée une boucle pour parcourir chaque élément de la liste.
Indices 2: vous pouvez travailler sur une liste dite copie avec [:].

"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
element = [2, 62, 13, 98, 80, 85, 77, 64, 83, 27, 45, 21, 28, 8, 82, 26, 87, 69, 85, 20, 41, 16, 11, 55, 43, 68, 96, 94, 52, 68]
# Résultat attendu :


# [2, 62, 98, 80, 64, 28, 8, 82, 26, 20, 16, 68, 96, 94, 52, 68]

"""
Rédige  un programme Python qui retire tout les elements impaire d'une liste.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée "element" et avoir pour résultat
 les variables: nouvelle_liste
"""


# Correction
def pair(input):
    nouvelle_liste = []
    for nombre in input:
        if nombre % 2 == 0:  # Vérifie si le nombre est pair
            nouvelle_liste += [nombre]  # Ajoute le nombre à la nouvelle liste
    return nouvelle_liste

output=pair(element)
print(output)
