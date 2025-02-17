"""
Lore :
Les Avengers se retrouvent face à une nouvelle menace d'intelligence artificielle créée par un ancien projet d'HYDRA.
Cette IA malveillante utilise des séquences numériques complexes pour déjouer les systèmes de défense des Avengers.
Tony Stark, déterminé à reprendre le contrôle, élabore un algorithme pour générer une liste de données numériques permettant de localiser les points faibles de l'IA.

Cependant, il doit d'abord établir une base : créer une liste contenant tous les éléments de 1 à 100,
qui serviront de points de référence pour le calcul. Le temps presse, et il doit se tourner vers
l'équipe pour l'aider à coder rapidement cette liste.

Bruce Banner suggère l'utilisation d'une boucle pour générer cette série d'éléments,
tandis que Natasha propose d'utiliser la méthode append() pour stocker les éléments dans une liste.
Ensemble, ils sont prêts à relever le défi et stopper l'IA avant qu'elle n'attaque.

Enoncé:

Écrire un programme Python pour creer une liste des element 1 a 100

Interdit : append()

Indices 1: Une boucle for peut être envisagée.
Indices 2:  ma_liste = ma_liste + ...


"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
ma_liste = []

# Résultat attendu :
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
# 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
# 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
# 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
# 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
# 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

"""
Rédige un programme pour ajouter a une liste les element de 1 a 100

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée ma_liste et avoir pour résultat
 les variables: ma_liste
"""


### Correction
def create_list():
    ma_liste = []
    for i in range(1, 101):
        ma_liste += [k]
    return ma_liste

output = create_list()

print(output)

