"""
Lore :
Les notes de l'examen de Botanique sont disponibles ! Quelle note as-tu eu ?

Enoncé :
Rédige une fonction qui prend en entrée le dictionnaire notes et la chaine de caractère nom_eleve. Cette fonction renvoie la note de l'élève à partir de la clé nom_eleve.
Si l'élève n'est pas dans le dictionnaire, elle renvoie -1.


Indice 1 : il faut en premier lieu vérifier la présence de la clé dans le dictionnaire
Indice 2 : l'opérateur in est utile pour vérifier la présence de la clé dans le dictionnaire
Indice 3 : pour récupérer la valeur du dictionnaire à partir de la clé, faire dictionnaire[cle]

Défi: utiliser une boucle while pour optimiser
"""

### Template fourni aux élèves

# Jeu de test
notes =  {
        "Potter": 16,
        "Granger": 20,
        "Weasley": 10,
        "Malfoy": 14,
        "Londubat": 18,
        "Patil": 15,
        "Goyle": 6,
        "Crabbe": 5,
        "Brown": 16,
        "Thomas": 9,
        "Finnigan":17,
    }

nom_eleve = "Londubat"

# Résultat attendu : recherche_note(notes) = 18

nom_eleve = "Lovegood"

# Résultat attendu : recherche_note(notes) = -1

"""
Complète la fonction en conservant sa signature
"""


def recherche_note(notes, nom_eleve):
    # Cette fonction renvoie un entier


### Correction

def recherche_note(notes, nom_eleve):
    if nom_eleve in notes:
        note = notes[nom_eleve]
    else:
        note = -1
    return note

