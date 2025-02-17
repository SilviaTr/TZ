"""
Lore :
Tu découvres un message secret d'un certain Tom Elvis Jedusor. De plus, après avoir fouillé dans la section interdite de la bibliothèque, tu trouves un grimoire qui semble contenir la solution pour décoder le message.

Enoncé : 
Pour réaliser cet exercice, deux entrées sont fournies.
Le message secret est le tableau message_secret dont chaque cellule contient une lettre.
Les permutations à effectuer sont contenues dans un second tableau, permutations : chaque cellule contient un tuple avec l'indice des cellules à échanger
Rédige un programme Python pour effectuer toutes les permutations et décoder le message.
Le résultat attendu est un tableau message_decode qui contient une lettre par cellule et qui correspondant au tableau message_secret après avoir appliqué toutes les permutations du tableau permutations.

Indice 1: tu as déjà réalisé une permutation lors de l'exercice sur les échecs
Indice 2: les tuples sont similaires aux listes, mais ils ne sont pas modifiables. Tu peux accéder aux élements des tuples de la liste permutations comme tu accéderais à l'élement d'une liste.

"""

### Template fourni aux élèves

# Jeu de données
message_secret = [
    "t",
    "o",
    "m",
    " ",
    "e",
    "l",
    "v",
    "i",
    "s",
    " ",
    "j",
    "e",
    "d",
    "u",
    "s",
    "o",
    "r",
]
permutations = [
    [10, 0],
    [4, 1],
    [3, 2],
    [8, 3],
    [13, 4],
    [7, 5],
    [14, 6],
    [9, 7],
    [14, 8],
    [13, 9],
    [13, 10],
    [12, 11],
    [14, 13],
    [15, 14],
    [16, 15],
]

# Résultat attendu :
message_decode = [
    "j",
    "e",
    " ",
    "s",
    "u",
    "i",
    "s",
    " ",
    "v",
    "o",
    "l",
    "d",
    "e",
    "m",
    "o",
    "r",
    "t",
]

"""
Rédige un programme pour réaliser toutes les permutations contenues dans le tableau permutations sur le tableau message_secret. 

/!\ Le programme solution de l'exercice doit bien utiliser les tableaux d'entrée message_secret et permutations et avoir pour résultat le tableau message_decode qui contient une lettre par cellule.
"""

### Correction
message_decode = message_secret
for permutation in permutations:
    tmp = message_decode[permutation[1]]
    message_decode[permutation[1]] = message_decode[permutation[0]]
    message_decode[permutation[0]] = tmp
    
