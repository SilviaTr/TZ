"""
/!\ Exercice qui peut être intéressant de reprendre quand on a vu les dictionnaires

Lore :
Vous collectionnez les cartes de chocogrenouilles. Vous voulez avoir une meilleure vision
de votre collection : 
1) Quelles sont les cartes que vous avez en doublons ?
2) Quelles sont les personnages que vous possédez ?
3) Quelles cartes sont manquantes ?

Enoncé :
1) Ecrire la fonction detect_doublons(collection) qui prend en entrée le tableau collection et renvoie
un tableau doublons qui contient toutes les cartes en doublon (une seule occurence de carte)

2) Ecrire la fonction collection_unique(collection) qui renvoie un tableau contenant toutes les cartes de la collection sans répétition. Cela signifie que si une collection contient des doublons, le tableau en sortie ne contiendra cette carte
qu'une seule fois.

3) Ecrire la fonction cartes_manquantes(collection, cartes_disponibles) qui renvoie un tableau contenant les cartes
manquantes à notre collection

Indice 1 : l'opérateur in et la méthode append pour les listes sont très utiles pour les 3 questions
Indice 2 : pour détecter les doublons, un tableau où tu stockes les cartes de la collection déjà rencontrées est utile

"""

### Template fourni aux élèves

# Jeux de test
collection1 = [
    "Rowena Serdaigle",
    "Paracelse",
    "Cliodna",
    "Gilderoy Lockhart",
    "Merlin",
    "Cliodna",
    "Nicholas Flamel",
    "Rowena Serdaigle",
    "Bridget Wenlock",
    "Paracelse",
    "Helga Poufsouffle",
    "Helga Poufsouffle",
    "Cliodna",
    "Musidora Barkwith",
]

collection2 = [
    "Argus Dumbledore",
    "Adalbert Waffling",
    "Morgane",
    "Paracelse",
    "Salazar Serpentard",
    "Nicholas Flamel",
    "Morgane",
    "Gilderoy Lockhart",
    "Musidora Barkwith",
    "Morgane",
    "Salazar Serpentard",
    "Helga Poufsouffle",
    "Nicholas Flamel",
    "Derwent Shimpling",
]

cartes_disponibles = [
    "Argus Dumbledore",
    "Merlin",
    "Gilderoy Lockhart",
    "Godric Griffondor",
    "Rowena Serdaigle",
    "Salazar Serpentard",
    "Helga Poufsouffle",
    "Nicholas Flamel",
    "Morgane",
    "Paracelse",
    "Adalbert Waffling",
    "Bridget Wenlock",
    "Musidora Barkwith",
    "Ignatia Wildsmith",
    "Bowman Wright",
    "Cliodna",
    "Derwent Shimpling",
    "Cassandra Vablatsky",
]


"""
Complète les fonctions sans changer les signatures
"""


def detect_doublons(collection):
    "renvoie un tableau doublons qui contient toutes les cartes en doublon (une seule occurence de carte)"


def collection_unique(collection):
    "renvoie un tableau contenant les cartes sans les doublons"


def cartes_manquantes(collection, cartes_disponibles):
    "renvoie un tableau contenant les cartes manquantes à notre collection"


### Correction


def detect_doublons(collection):
    doublons = []
    cartes_classees = []
    for carte in collection:
        if carte in cartes_classees and carte not in doublons:
            doublons.append(carte)
        cartes_classees.append(carte)
    return doublons


def collection_unique(collection):
    collection_sans_doublons = []
    for carte in collection:
        if carte not in collection_sans_doublons:
            collection_sans_doublons.append(carte)
    return collection_sans_doublons


def cartes_manquantes(collection, cartes_disponibles):
    cartes_pas_dans_collection = []
    for carte in cartes_disponibles:
        if carte not in collection:
            cartes_pas_dans_collection.append(carte)
    return cartes_pas_dans_collection
