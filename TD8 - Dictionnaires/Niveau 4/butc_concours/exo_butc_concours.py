"""
Lore :
La bibliothèque souhaite organiser un concours pour récompenser les livres les plus appréciés par les lecteurs. Les livres seront jugés sur plusieurs critères :
- Note moyenne
- Nombre de votes
- Catégorie

Les critères de sélection des livres gagnants sont les suivants :
- Pour chaque catégorie, sélectionner le livre avec la note moyenne la plus élevée.
- En cas d'égalité de note moyenne, sélectionner le livre avec le plus grand nombre de votes.
- En cas d'égalité de votes, sélectionner le livre le plus ancien (avec l'année de publication la plus basse).

Énoncé :
Rédige une fonction qui prend en entrée une liste de dictionnaires correspondant aux livres. Chaque dictionnaire décrit un livre par son titre, auteur, catégorie, note moyenne, nombre de votes et année de publication.
Cette fonction doit renvoyer un dictionnaire où chaque clé est une catégorie et la valeur associée est le livre gagnant de cette catégorie respectant les conditions décrites ci-dessus.

Interdit : utilisation de sorted()

Indice 1 : Pour chaque catégorie, utilise un dictionnaire pour stocker les livres de cette catégorie.
Indice 2 : Pour chaque catégorie, parcours la liste des livres pour trouver le livre gagnant en fonction des critères.
Indice 3 : Parcours la liste des livres une fois pour les regrouper par catégorie, puis une deuxième fois pour déterminer le gagnant de chaque catégorie.
Indice 4 :  Fais attention à bien respecter les critères de sélection.
"""

### Template fourni aux élèves
 
# Jeu de test
 
livres = [ 
    {"titre": "Harry Potter", "auteur": "J.K. Rowling", "categorie": "Fantastique", "note_moyenne": 4.9, "votes": 1000000, "annee": 1997}, 
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "categorie": "Fiction", "note_moyenne": 4.8, "votes": 500000, "annee": 1943}, 
    {"titre": "1984", "auteur": "George Orwell", "categorie": "Fiction", "note_moyenne": 4.8, "votes": 600000, "annee": 1949}, 
    {"titre": "Python pour les Nuls", "auteur": "John Paul Mueller", "categorie": "Informatique", "note_moyenne": 4.5, "votes": 250000, "annee": 2015}, 
    {"titre": "L'Étranger", "auteur": "Albert Camus", "categorie": "Littérature", "note_moyenne": 4.3, "votes": 300000, "annee": 1942}, 
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "categorie": "Fantastique", "note_moyenne": 4.9, "votes": 800000, "annee": 1954}, 
    {"titre": "La Ferme des Animaux", "auteur": "George Orwell", "categorie": "Fiction", "note_moyenne": 4.7, "votes": 400000, "annee": 1945} 
]


# Résultat attendu :
"""
livres_gagnants(livres) = {
    'Fantastique': {'titre': 'Harry Potter', 'auteur': 'J.K. Rowling', 'categorie': 'Fantastique', 'note_moyenne': 4.9, 'votes': 1000000, 'annee': 1997}, 
    'Fiction': {'titre': '1984', 'auteur': 'George Orwell', 'categorie': 'Fiction', 'note_moyenne': 4.8, 'votes': 600000, 'annee': 1949}, 
    'Informatique': {'titre': 'Python pour les Nuls', 'auteur': 'John Paul Mueller', 'categorie': 'Informatique', 'note_moyenne': 4.5, 'votes': 250000, 'annee': 2015}, 
    'Littérature': {'titre': "L'Étranger", 'auteur': 'Albert Camus', 'categorie': 'Littérature', 'note_moyenne': 4.3, 'votes': 300000, 'annee': 1942}
}
"""

"""
Complète la fonction en conservant sa signature
"""
 
def livres_gagnants(livres): 
    # Cette fonction renvoie un dictionnaire
    return

### Correction
def livres_gagnants(livres): 
    categories = {} 
    for livre in livres: 
        categorie = livre["categorie"] 
        if categorie not in categories: 
            categories[categorie] = [] 
        categories[categorie].append(livre)
    gagnants = {}
    for categorie, livres_liste in categories.items():
        meilleur_livre = livres_liste[0]
        for livre in livres_liste:
            if (
                livre["note_moyenne"] > meilleur_livre["note_moyenne"] or
                (livre["note_moyenne"] == meilleur_livre["note_moyenne"] and livre["votes"] > meilleur_livre["votes"]) or
                (livre["note_moyenne"] == meilleur_livre["note_moyenne"] and livre["votes"] == meilleur_livre["votes"] and livre["annee"] < meilleur_livre["annee"])
            ):
                meilleur_livre = livre
        gagnants[categorie] = meilleur_livre
    return gagnants
