"""
Lore :
La BUTC doit faire l'inventaire des livres pour savoir combien de chaque genre ils ont en stock.

Enoncé :
La liste stock contient les différents genres de livres disponibles à la BUTC. 
Chaque genre peut être présent en plusieurs exemplaires. 
À l'aide d'un dictionnaire inventaire, compte le nombre de livres de chaque genre actuellement disponible en bibliothèque.

Interdit : utilisation de get()

Indice 1 : Initialisez un dictionnaire vide pour l'inventaire.
Indice 2 : Parcourez la liste stock avec une boucle for.
Indice 3 : Pour chaque genre, vérifiez s'il est déjà dans le dictionnaire inventaire.
Indice 4 : Si le genre est déjà dans le dictionnaire, incrémentez sa valeur de 1.
Indice 5 : Si le genre n'est pas dans le dictionnaire, ajoutez-le avec une valeur de 1.

"""

### Template fourni aux élèves

## Jeu de test
stock = [
    "Fiction",
    "Informatique",
    "Littérature",
    "Fantasy",
    "Informatique",
    "Fiction",
    "Fantasy",
    "Littérature",
    "Fiction",
    "Informatique",
    "Fantasy",
    "Fiction",
]

"""
Complète la fonction
"""

def faire_inventaire(stock):
    # Cette fonction renvoie un dictionnaire
    return 

### Correction
def faire_inventaire(stock):
    inventaire = {}
    for genre in stock:
        if genre in inventaire:
            inventaire[genre] += 1
        else:
            inventaire[genre] = 1
    return inventaire
