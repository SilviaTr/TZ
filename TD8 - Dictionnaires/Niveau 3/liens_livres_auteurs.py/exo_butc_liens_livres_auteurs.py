
"""
Lore :
Le bibliothécaire se demande s'il y a un lien entre les genres des livres et les auteurs.

Enoncé :

Sur l'échantillon fourni :
Quel est le genre de prédilection de l'auteur "J.K. Rowling" ?
Quel auteur a le plus de livres de genre "Fiction" ?
Quel auteur a en moyenne les livres les plus longs (en nombre de pages) ?

Interdit : utilisation de get() et max()

Indice 1 : Pour le genre de prédilection, utilise un dictionnaire pour compter les occurrences de chaque genre pour l'auteur donné.
Indice 2 : Pour l'auteur avec le plus de livres de genre "Fiction", utilise un dictionnaire pour compter les occurrences de chaque auteur pour ce genre.
Indice 3 : Pour l'auteur avec les livres les plus longs, utilise deux dictionnaires : un pour la somme des pages et un pour le nombre de livres par auteur. Calcule ensuite la moyenne des pages pour chaque auteur.
Indice 4 : Trouver les valeurs maximales ou minimales dans les dictionnaires en parcourant les éléments.

"""

### Template fourni aux élèves

## Jeu de test
livres = [
    {"titre": "Harry Potter", "auteur": "J.K. Rowling", "genre": "Fantasy", "pages": 500},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "genre": "Fiction", "pages": 96},
    {"titre": "1984", "auteur": "George Orwell", "genre": "Fiction", "pages": 328},
    {"titre": "Python pour les Nuls", "auteur": "John Paul Mueller", "genre": "Informatique", "pages": 432},
    {"titre": "L'Étranger", "auteur": "Albert Camus", "genre": "Littérature", "pages": 123},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "genre": "Fantasy", "pages": 1216},
    {"titre": "Animal Farm", "auteur": "George Orwell", "genre": "Fiction", "pages": 112},
]

# Résultat attendu :
# genre_predilection(livres, "J.K. Rowling") = "Fantasy"
# auteur_fiction(livres) = "George Orwell"
# auteur_livres_longs(livres) = "J.R.R. Tolkien"

"""
Complète les fonctions en conservant leur signature
"""

def genre_predilection(livres, auteur):
   # Cette fonction renvoie une chaîne de caractères
    return 

def auteur_fiction(livres):
    # Cette fonction renvoie une chaîne de caractères
    return 

def auteur_livres_longs(livres):
    # Cette fonction renvoie une chaîne de caractères
    return 

# Correction
def genre_predilection(livres, auteur):
    count_genre = {}
    for livre in livres:
        if livre["auteur"] == auteur:
            genre = livre["genre"]
            if genre in count_genre:
                count_genre[genre] += 1
            else:
                count_genre[genre] = 1
    # Trouver le genre avec le maximum d'occurrences
    max_genre = None
    max_count = -1
    for genre, count in count_genre.items():
        if count > max_count:
            max_genre = genre
            max_count = count
    return max_genre

def auteur_fiction(livres):
    count_auteur = {}
    for livre in livres:
        if livre["genre"] == "Fiction":
            auteur = livre["auteur"]
            if auteur in count_auteur:
                count_auteur[auteur] += 1
            else:
                count_auteur[auteur] = 1
     # Trouver l'auteur avec le maximum de livres de genre "Fiction"
    max_auteur = None
    max_count = -1
    for auteur, count in count_auteur.items():
        if count > max_count:
            max_auteur = auteur
            max_count = count
    return max_auteur

def auteur_livres_longs(livres):
    total_pages = {}
    count_livres = {}
    for livre in livres:
        auteur = livre["auteur"]
        pages = livre["pages"]
        if auteur in total_pages:
            total_pages[auteur] += pages
            count_livres[auteur] += 1
        else:
            total_pages[auteur] = pages
            count_livres[auteur] = 1
    avg_pages = {auteur: total_pages[auteur] / count_livres[auteur] for auteur in total_pages}
    # Trouver l'auteur avec la moyenne de pages la plus élevée
    max_auteur = None
    max_avg = -1
    for auteur, avg in avg_pages.items():
        if avg > max_avg:
            max_auteur = auteur
            max_avg = avg
    return max_auteur
