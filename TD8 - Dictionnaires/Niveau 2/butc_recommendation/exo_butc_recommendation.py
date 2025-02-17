"""
Lore :
La BUTC souhaite recommander des livres aux lecteurs en fonction de leurs préférences.

Enoncé :
Rédige une fonction qui recommande le premier livre qui correspond au lecteur à partir de 3 caractéristiques (genre préféré, auteur préféré, nombre de pages préféré). 
Les caractéristiques des livres disponibles sont fournies. En cas d'égalité, applique la priorité suivante : genre > auteur > nombre de pages.

Interdit : utilisation de get()

Indice 1 : Parcourt la liste des livres avec une boucle for.
Indice 2 : Vérifie d'abord si le genre du livre correspond au genre préféré.
Indice 3 : Si aucun livre ne correspond au genre préféré, vérifie si l'auteur du livre correspond à l'auteur préféré.
Indice 4 : Si aucun livre ne correspond à l'auteur préféré, vérifie si le nombre de pages du livre correspond au nombre de pages préféré.
Indice 5 : Retourne le titre du premier livre qui correspond à l'une des préférences, en respectant l'ordre de priorité.


"""


### Template fourni aux élèves

## Jeu de test
livres = [
    {"titre": "Harry Potter", "auteur": "J.K. Rowling", "genre": "Fantasy", "pages": 500, "longueur": "moyen"},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "genre": "Fiction", "pages": 96, "longueur": "court"},
    {"titre": "1984", "auteur": "George Orwell", "genre": "Fiction", "pages": 328, "longueur": "moyen"},
    {"titre": "Python pour les Nuls", "auteur": "John Paul Mueller", "genre": "Informatique", "pages": 432, "longueur": "moyen"},
    {"titre": "L'Étranger", "auteur": "Albert Camus", "genre": "Littérature", "pages": 123, "longueur": "court"},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "genre": "Fantasy", "pages": 1216, "longueur": "long"},
    {"titre": "Animal Farm", "auteur": "George Orwell", "genre": "Fiction", "pages": 112, "longueur": "court"},
]


"""
Complète la fonction 
"""
def recommander_livre(livres, genre_prefere, auteur_prefere, pages_preferees):
    # cette fonction renvoie une chaîne de caractères (le titre du livre recommandé)
    return 

# Résultat attendu
# recommander_livre('Fiction', 'George Orwell', 'court') = 'Le Petit Prince'
# recommander_livre('Art', 'George Orwell', 'long') = '1984' 
# recommander_livre('Art', 'Recueil', 'long') = 'Le Seigneur des Anneaux'
# recommander_livre('Art', 'Recueil', 'très court') = 'Aucun livre ne correspond à vos préférences'

### Correction
def recommander_livre(livres, genre_prefere, auteur_prefere, pages_preferees):
    for livre in livres:
        if livre["genre"] == genre_prefere:
            return livre["titre"]
        if livre["auteur"] == auteur_prefere:
            return livre["titre"]
        if livre["longueur"] == pages_preferees:
            return livre["titre"]
    return "Aucun livre ne correspond à vos préférences"



