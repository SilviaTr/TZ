"""
Lore :
Le prof de "Défense contre les forces du mal" Gilderoy Lockhear a de grandes difficultés pour calculer la moyenne
de ses examens. Aide le en lui apprenant un nouveau sort qui calcule automatiquement la moyenne.

Enoncé :
A partir d'un tableau "notes" fourni, écris un programme Python pour calculer la moyenne des valeurs contenues dans le tableau. La variable contenant le résultat a pour nom "moyenne"

Interdit : utilisation des fonctions sum et mean.

Indice 1 : Calculer la moyenne du tableau revient à faire la somme de toutes les valeurs, divisée par le nombre de valeurs.
Indice 2 : Une boucle for permet de parcourir le tableau pour calculer la somme des valeurs. Tu peux commencer par afficher toutes les valeurs du tableau pour tester ta boucle !
Indice 3 : Crée une variable pour stocker la somme des valeurs. A chaque itération de la boucle, ajoute la valeur lue à la somme.
Indice 4 : Est-ce que tu as initialisé la variable qui stocke ta somme à 0 ? 
"""


### Template fourni aux élèves

# Jeux de test
notes1 = [14, 15, 16]        # Résultat attendu: moyenne = 15
notes2 = [0, 5, 10, 10, 15, 20]                    # Résultat attendu: moyenne = 10
notes3 = [11, 13, 15, 9, 12, 5, 12, 11, 7, 13, 18, 11, 3, 14]      # Résultat attendu: moyenne = 11

"""
Rédige un programme pour calculer la moyenne du tableau notes

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée notes et avoir pour résultat la variable moyenne
"""


### Correction

somme = 0
for note in notes:
    somme += note

moyenne = somme / len(tab)

# Ce n'est pas le but de l'exercice ici, mais la fonction sum et mean existe pour simplifier tes codes futurs.