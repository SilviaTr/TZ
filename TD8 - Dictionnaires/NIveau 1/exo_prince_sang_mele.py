"""
Lore :
Harry a trouvé un livre lors du cours de potions du Professeur Slughorn. Ce dernier appartenait au "Prince de Sang-Mêlé", un sorcier de génie qui a même inventé de nouveaux sortilèges.
Vous essayez d'aider Harry à découvrir la véritable identité du Prince de Sang-Mêlé.

Enoncé :
Rédige une fonction qui prend en entrée une liste de dictionnaires. Chaque dictionnaire décrit un individu par son nom, prénom, surnom et maison.
Cette fonction renvoie le nom de l'individu dont le surnom est "Le Prince de Sang-Mêlé". S'il n'existe pas, il renvoie une chaine de caractères vide


Indice 1 : Parcourir la liste en testant pour chaque individu si son surnom est "Le Prince de Sang-Mêlé"
Indice 2 : Pour optimiser la recherche, il est préférable d'utiliser une boucle while qui s'arrête lorsque l'individu a été trouvé

Défi: utiliser une boucle while pour optimiser
"""

### Template fourni aux élèves

# Jeux de test
suspects = [
    {
        "prenom": "Harry",
        "nom": "Potter",
        "surnom": "Le Garçon Qui a Survécu",
        "maison": "Gryffondor"
    },
    {
        "prenom": "Ronald",
        "nom": "Weasley",
        "surnom": "Ron",
        "maison": "Gryffondor"
    },
    {
        "prenom": "Sirius",
        "nom": "Black",
        "surnom": "Padfoot",
        "maison": "Gryffondor"
    },
    {
        "prenom": "Severus",
        "nom": "Rogue",
        "surnom": "Le Prince de Sang-Mêlé",
        "maison": "Serpentard"
    },
    {
        "prenom": "Tom",
        "nom": "Riddle",
        "surnom": "Voldemort",
        "maison": "Serpentard"
    }
]


# Résultat attendu : recherche_prince(suspects) = "Rogue"

"""
Complète la fonction en conservant sa signature
"""


def recherche_prince(suspects):
    # Cette fonction renvoie une chaine de caractère


### Correction

def recherche_prince(suspects):
    j=0
    nom_prince = ""
    while len(nom_prince)==0 or j<(len(suspects)-1):
        if suspects[j]["surnom"]=="Le Prince de Sang-Mêlé":
            nom_prince = suspects[j]["nom"]
        j+=1
    return nom_prince

