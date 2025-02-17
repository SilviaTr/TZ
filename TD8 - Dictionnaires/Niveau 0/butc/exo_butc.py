"""
Lore :
La BUTC vient de recevoir une nouvelle collection de livres. Le bibliothécaire doit organiser ces livres par genre.

Enoncé :
Crée un dictionnaire qui répertorie les titres et genres des livres suivants :
"Le Petit Prince" : Fiction
"Python pour les Nuls" : Informatique
"L'Étranger" : Littérature
 
La clé du dictionnaire sera le titre du livre et la valeur sera le genre.

Indice 1 : Un dictionnaire en Python se crée avec des accolades {}.
Indice 2 : Les clés du dictionnaire seront les titres des livres.
Indice 3 : Les valeurs du dictionnaire seront les genres des livres.
Indice 4 : Tu peux créer le dictionnaire directement avec toutes les paires clé-valeur ou ajouter les paires une par une.
"""

### Template fourni aux élèves

"""
Crée le dictionnaire répertoriant les titres et genres des livres
"""
def collection():
    livres = {
        #à remplir
    }
    return livres  

### Correction
def collection():
    livres = {
        "Le Petit Prince": "Fiction",
        "Python pour les Nuls": "Informatique",
        "L'Étranger": "Littérature"
    }
    return livres  