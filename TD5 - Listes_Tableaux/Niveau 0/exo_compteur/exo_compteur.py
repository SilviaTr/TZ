

"""
Lore :
Alors que les Avengers se préparent à une nouvelle menace galactique,
Vision est chargé d'analyser d'énormes bases de données interstellaires pour y détecter des schémas cachés. Cependant,
ces données sont corrompues et les systèmes ne peuvent pas mesurer correctement leur taille. Vision doit trouver une solution.
Privé de sa capacité à utiliser les outils classiques comme len(), il doit trouver une solution!!!

Enoncé:

Écrire un programme Python pour compter les elements d'une liste

Interdit : len()

Indices 1: crée une boucle
Indices 2: initialiser un compteur à 0


"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
planets  = [
    'Orion', 'Scorpion', 'Cassiopeia', 'Andromède', 'Lyre', 'Cygne', 'Taureau',
    'Bélier', 'Vierge', 'Lion', 'Poissons', 'Balance', 'Sagittaire', 'Verseau',
    'Capricorne', 'Gémeaux', 'Cancer', 'Pégase', 'Hercule', 'Hydre',
    'Mars', 'Jupiter', 'Saturne', 'Vénus', 'Mercure', 'Neptune', 'Uranus',
    'Pluton', 'Terre', 'Proxima Centauri b', 'Kepler-22b', 'TRAPPIST-1e',
    'GJ 1214b', 'Gliese 581g', 'HD 40307g', 'WASP-12b', 'LHS 1140b',
    'Kepler-452b']

# Résultat attendu : 38
#

"""
Rédige un programme pour ajouter a une liste les element de 1 a 100

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée "planets" et avoir pour résultat
 les variables: nombre
"""


### Correction
# Code de départ


def compteur(input):
    nombre = 0
    for k in input:
        nombre += 1
    return nombre



