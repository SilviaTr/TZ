"""
Lore :
En tant que collectionneur de figurines des super-héros Marvel, vous souhaitez avoir une meilleure vision
de votre collection :
1) Quelles figurines avez-vous en doublons ?
2) Quels personnages possédez-vous ?
3) Quelles figurines vous manquent ?

Enoncé :
1) Écrire la fonction detect_doublons(collection) qui prend en entrée le tableau collection et renvoie
un tableau doublons qui contient toutes les figurines en doublon (une seule occurrence de figurine).

2) Écrire la fonction collection_unique(collection) qui renvoie un tableau contenant toutes les figurines
de la collection sans répétition. Cela signifie que si une collection contient des doublons, le tableau
en sortie ne contiendra cette figurine qu'une seule fois.

3) Écrire la fonction figurines_manquantes(collection, figurines_disponibles) qui renvoie un tableau
contenant les figurines manquantes à notre collection.

Indice 1 : l'opérateur in et la méthode append pour les listes sont très utiles pour les 3 questions.
Indice 2 : pour détecter les doublons, un tableau où tu stockes les figurines de la collection déjà rencontrées
est utile.
"""

### Template fourni aux élèves

# Jeux de test
collection1 = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Black Widow",
    "Hulk",
    "Thor",
    "Spider-Man",
    "Iron Man",
    "Doctor Strange",
    "Black Widow",
    "Hawkeye",
    "Hawkeye",
    "Thor",
    "Vision",
]

collection2 = [
    "Black Panther",
    "Wolverine",
    "Scarlet Witch",
    "Doctor Strange",
    "Spider-Man",
    "Scarlet Witch",
    "Captain America",
    "Hawkeye",
    "Iron Man",
    "Scarlet Witch",
    "Vision",
    "Hulk",
    "Doctor Strange",
    "Groot",
]

figurines_disponibles = [
    "Black Panther",
    "Iron Man",
    "Captain America",
    "Spider-Man",
    "Thor",
    "Black Widow",
    "Doctor Strange",
    "Hulk",
    "Scarlet Witch",
    "Vision",
    "Groot",
    "Wolverine",
    "Hawkeye",
    "Deadpool",
]

"""
Complète les fonctions sans changer les signatures


def reparo(collection, figurines_disponibles):
    def detect_doublons(collection):
         "renvoie un tableau doublons qui contient toutes les figurines en doublon (une seule occurrence de figurine)"

        return doublons

    def collection_unique(collection):
            "renvoie un tableau contenant les figurines sans les doublons"

        
        return collection_sans_doublons

    def figurines_manquantes(collection, figurines_disponibles):
        
            "renvoie un tableau contenant les figurines manquantes à notre collection"

        return figurine
    
    return [doublons, collection_sans_doublons, figurines_pas_dans_collection]  


"""

### Correction




def correction(collection, figurines_disponibles):
    def detect_doublons(collection):
        doublons = []
        figurines_classees = []
        for figurine in collection:
            if figurine in figurines_classees and figurine not in doublons:
                doublons.append(figurine)
            figurines_classees.append(figurine)
        return doublons

    def collection_unique(collection):
        collection_sans_doublons = []
        for figurine in collection:
            if figurine not in collection_sans_doublons:
                collection_sans_doublons.append(figurine)
        return collection_sans_doublons

    def figurines_manquantes(collection, figurines_disponibles):
        return [figurine for figurine in figurines_disponibles if figurine not in collection]

    return detect_doublons(collection), collection_unique(collection), figurines_manquantes(collection, figurines_disponibles)
