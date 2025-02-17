"""
Lore :
Fred et Georges Weasley ont ouvert un nouveau magasin : "Weasley, Farces pour sorciers facétieux".
La boutique est un franc succès et ils réalisent l'inventaire des stocks pour déterminer ce qu'il doit racheter.

Enoncé : 
La liste stock contient les différents produits disponibles dans le magasin. Chaque produit peut être présent en plusieurs exemplaires.
A l'aide d'un dictionnaire inventaire, comptez le nombre de produits actuellement disponibles en magasin.


Indice 1 : Le dictionnaire inventaire doit avoir pour clé les produits de la liste stock et comme valeur le nombre de chacun des produits
Indice 2 : Pour chaque produit, deux cas sont à prendre en compte : il est déjà présent dans le dictionnaire ou non
Indice 3 : Le test d'appartenance se fait avec l'opérateur in

"""

### Template fourni aux élèves

# Jeux de test
stock = [
    "chaudron farceur",
    "leurre explosif",
    "télescope frappeur",
    "leurre explosif",
    "marécage potable",
    "plume",
    "boite à flemme",
    "chapeau bouclier",
    "plume",
    "philtre d'amour",
    "leurre explosif",
    "cape bouclier",
    "chaudron farceur",
    "plume",
    "boite à flemme",
    "leurre explosif",
    "plume",
    "chapeau bouclier",
    "plume",
    "télescope frappeur",
    "boite à flemme",
    "boite à flemme",
    "leurre explosif",
    "plume",
]

"""
Complète la fonction en conservant sa signature
"""


def faire_inventaire(stocks):
    # Cette fonction renvoie un dictionnaire

### Correction

def faire_inventaire(stocks):
    inventaire = {}
    for produit in stocks:
        if produit in inventaire:
            inventaire[produit] += 1
        else:
            inventaire[produit] = 1
    return inventaire

### Contraintes à appliquer lors de l'implémentation du jeu de données

"""

* Pas de réussite si on utilise pas un dictionnaire
* Faire perdre des points si on utilise une liste en plus ?
* Empêcher ou faire perdre des points si l'utilisateur utilise plusieurs for


"""