"""
Lore :
Les notes des critiques littéraires sont disponibles ! Quelle note a reçu chaque livre ?

Enoncé :
Rédige une fonction qui prend en entrée le dictionnaire notes et la chaîne de caractères titre_livre. 
Cette fonction renvoie la note du livre à partir de la clé titre_livre. Si le livre n'est pas dans le dictionnaire, elle renvoie -1.

Interdit : utilisation de get()

Indice 1 : Utilise l'opérateur in pour vérifier si une clé existe dans le dictionnaire.
Indice 2 : Si la clé existe, utilise dictionnaire[cle] pour obtenir la valeur associée.
Indice 3 : Si la clé n'existe pas, retourne -1.
Indice 4 : Utilise une structure conditionnelle if-else pour gérer les deux cas.


"""

### Template fourni aux élèves

## Jeu de test
notes = {
    "Le Petit Prince": 9,
    "Python pour les Nuls": 7,
    "L'Étranger": 8,
    "Le Seigneur des Anneaux": 10,
    "1984": 9,
    "Harry Potter": 10,
}

titre_livre = "L'Étranger"
# Résultat attendu : recherche_note_livre(notes, titre_livre) = 8

titre_livre = "Le Hobbit"
# Résultat attendu : recherche_note_livre(notes, titre_livre) = -1

"""
Complète la fonction 
"""

def recherche_note_livre(notes, titre_livre):
    # Cette fonction renvoie un entier
    return

### Correction
def recherche_note_livre(notes, titre_livre):
    if titre_livre in notes:
        return notes[titre_livre]
    else:
        return -1
