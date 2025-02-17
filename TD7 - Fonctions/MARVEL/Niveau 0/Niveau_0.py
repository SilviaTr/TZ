"""
Lore :
Tony Stark a récemment écrit un manuel intitulé 'Stratégies de Défense Avancée avec la Technologie Stark' pour aider les Avengers à mieux se préparer aux menaces. Cependant, avec toutes les attaques imminentes, il n'a pas le temps de distribuer les exemplaires. 
Tu décides donc d'aider Tony en développant une IA qui pourrait recopier automatiquement le texte autant de fois que nécessaire.

Enoncé :
Rédiger une procédure qui prend en entrée un texte et le nombre n de fois dont le texte doit être recopié.
La procédure affiche le texte n fois (séparé par un tiret).


Indice 1: utilise une boucle "if" pour faire des itérations n fois
Indice 2: Ajoute chaque itération du texte à une variable solution avec un tiret
Indice 3: retourne la variable solution

"""

### Template fourni aux élèves

texte = "La clé de la défense avancée réside dans la technologie. Comme Tony Stark le dit souvent, 'Une technologie bien pensée vaut mieux que dix super-soldats.' \
    La préparation implique de connaître les systèmes défensifs, les contre-mesures automatiques et les moyens de renforcer la sécurité autour des Avengers. \
    Un Avenger bien équipé est prêt à faire face aux menaces, qu'elles viennent de l'espace ou de la Terre. Un autre principe clé de la défense avancée est la concentration. \
    Dans les situations de crise, il est crucial de se concentrer sur la menace immédiate. Les systèmes défensifs demandent une précision extrême, \
    et toute distraction pourrait être fatale. Les Avengers doivent rester focalisés, même sous pression, car cela peut signifier la différence entre sauver la planète ou la perdre."

"""
Rédige une procédure pour recopier ce texte n fois.
Garde la même signature pour la procédure !
"""


def copie(texte, n):
    "écrit ton code ici"
    


### Correction


def copie(texte, n):
    solution = ""
    for i in range(n):
        solution += texte
        solution += " - "
    return solution

