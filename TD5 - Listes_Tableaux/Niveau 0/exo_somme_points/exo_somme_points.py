"""
Lore :
Pour ajuster son système de points, Dumbledore aimerait connaitre le total des points attribués à chacune des maisons, sans compter les pénalités appliquées.

Enoncé :
A partir d'un tableau contenant des valeurs positives et négatives, faire un programme Python qui ne réalise la somme que des nombres positifs

Interdit : utilisation des fonctions sum.

Indice 1 : Une boucle for permet de parcourir le tableau pour calculer la somme des valeurs.
Indice 2 : Une condition if te permet de tester si les valeurs du tableau sont bien positives
Indice 3 : Crée une variable pour stocker la somme des valeurs. A chaque itération de la boucle, ajoute la valeur lue à la somme.
Indice 4 : Est-ce que tu as initialisé la variable qui stocke ta somme à 0 ? 
"""


### Template fourni aux élèves

# Jeux de test
gryffondor = [-1, -1, 5, -5, 5, 5, -5, -5, 100, -50, -50, -50, 50, 50, 60, 10]        # Résultat attendu: somme = 285
serdaigle = [5, 10, -1, -5, 10, 15, -5, -1, -1, 20, 10, -5, -5, -5, 10]                    # Résultat attendu: moyenne = 80
serpentard = [-1, -1, -1, -1, -20, -5, 10, 5, -1, 20, 5, 5, -1, -1, -1, 10]      # Résultat attendu: somme = 55
poufsouffle = [5, 5, -1, -5, -1, 5, 5, -5, 10, -1, -1, 10, -5, 10]              # Résultat attendu : somme = 50

"""
Rédige un programme pour calculer la somme des nombre positis

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée points et avoir pour résultat la variable somme
"""


### Correction

somme = 0
for point in points:
    if point >0:
        somme += point

