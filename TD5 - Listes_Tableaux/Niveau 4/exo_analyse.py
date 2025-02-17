

"""
Lore :
Tony Stark est en train de passer en revue les statistiques de ses anciennes armures pour comprendre lesquelles sont les plus efficaces.
Chaque modèle d'armure est représenté par un ensemble de valeurs comme la vitesse, la résistance ou l'efficacité énergétique.
Pour prendre une décision éclairée, Tony doit calculer plusieurs indicateurs statistiques à partir des données
récoltées : la moyenne des performances, la médiane des résultats, ainsi que la variance et l’écart type.

Avec son esprit scientifique aiguisé, Tony écrit un programme en Python pour automatiser ce processus.
Grâce à cet algorithme, il peut identifier la stabilité des performances de ses armures et repérer les modèles qui
sortent du lot, lui permettant de concentrer ses efforts de développement sur les designs les plus prometteurs.

Ce programme devient crucial pour ses futures batailles, car il permet d’optimiser les armures
en fonction des résultats statistiques et d’améliorer ses performances en temps réel.

Chaque ligne transposée reflète une force prête à défendre la réalité contre les forces du chaos.

Énoncé :

Écrire un programme Python qui, à partir d'une liste deja triée de nombres, calcule les statistiques suivantes :


La moyenne de la liste.
La médiane de la liste (en triant les nombres et en prenant l'élément du milieu, ou la moyenne des deux du milieu si la liste a un nombre pair d'éléments).
La variance de la liste (moyenne des carrés des écarts par rapport à la moyenne).
L'écart type (racine carrée de la variance).


Exigences :
Utilisez une approche manuelle, sans l'aide de bibliothèques comme statistics.
Assurez-vous que le programme puisse s'adapter à n'importe quelle taille de liste.


"""

### Template fourni aux élèves

# Jeux de test
stats_armures = [85.5, 90.3, 95.0, 100.1, 105.7, 110.5, 115.9, 120.0, 125.4, 130.2]
#resulat :
#Moyenne : 107.85999999999999
#Médiane : 108.1
#variance : 206.43040000000002
#Écart type : 14.367685965387746


"""
Rédige Écrire un programme Python qui, à partir d'une liste deja triée de nombres, calcule les statistiques suivantes :

La moyenne de la liste.
La médiane de la liste (en triant les nombres et en prenant l'élément du milieu, ou la moyenne des deux du milieu si la liste a un nombre pair d'éléments).
La variance de la liste (moyenne des carrés des écarts par rapport à la moyenne).
L'écart type (racine carrée de la variance).

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées stats_armures et avoir pour résultat
 les variables: moyenne, mediane, variance, ecart_type
"""

### Correction
def analyse(input):
    somme = 0
    for nombre in input:
        somme += nombre
    moyenne = somme / len(input)
    n = len(input)
    if n % 2 == 0:
        mediane = (input[n // 2 - 1] + input[n // 2]) / 2
    else:
        mediane = input[n // 2]

    variance = 0
    for nombre in input:
        variance += (nombre - moyenne) ** 2
    variance /= len(input)
    ecart_type = variance ** 0.5
    return moyenne, mediane, variance, ecart_type

output =  analyse( stats_armures)
print( analyse(input))



