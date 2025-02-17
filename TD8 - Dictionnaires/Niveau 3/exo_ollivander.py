"""
Lore :
Ollivander se demande s'il y a un lien entre les propriétés des baguettes et la maison de son sorcier propriétaire à Poudlard. En effet, la baguette choisit son sorcier...

Enoncé : sur l'échantillon fourni:
1) Quel est le type de bois de prédilection pour les Serpentard ?
2) Quel maison a le plus de baguette dont le coeur est en plume de phénix ?
3) Quel maison a en moyenne les baguettes les plus courtes ?



Indice 1 : si vous avez des difficultés à compter le nombre d'occurence d'un élément dans un dictionnaire, refaire l'exercice précédent pourra vous aider
Indice 2 : pour récupérer l'élément avec le plus ou le moins d'occurence, les fonctions min et max sont pratiques. Pour que cela fonctionne, il faut utiliser l'argument key. 
Indice 3 : l'élément baguette du dictionnaire est lui même un dictionnaire. Pour accéder au élément "bois" de la baguette "bag", faire bag["baguette]["bois"]
Indice 4 : pour calculer la moyenne des longueurs de baguettes par maison, 2 dictionnaires avec pour clé le nom des maisons vont seront utiles
Indice 5 : le premier dictionnaire permet de faire la somme des longueurs des baguettes et le second permet de compter le nombre de baguette par maison.

"""

### Template fourni aux élèves

# Jeux de test
liste_baguettes = [
    {
        "maison": "Gryffondor",
        "baguette": {"bois": "houx", "coeur": "plume de phénix", "longueur": 27},
    },
    {
        "maison": "Gryffondor",
        "baguette": {"bois": "vigne", "coeur": "ventricule de dragon", "longueur": 27},
    },
    {
        "maison": "Serdaigle",
        "baguette": {"bois": "roseau", "coeur": "corne de basilic", "longueur": 13},
    },
    {
        "maison": "Gryffondor",
        "baguette": {"bois": "saule", "coeur": "crin de licorne", "longueur": 35},
    },
    {
        "maison": "Serpentard",
        "baguette": {"bois": "aubépine", "coeur": "crin de licorne", "longueur": 25},
    },
    {
        "maison": "Serdaigle",
        "baguette": {"bois": "sapin", "coeur": "ventricule de dragon", "longueur": 27},
    },
    {
        "maison": "Gryffondor",
        "baguette": {"bois": "saule", "coeur": "crin de licorne", "longueur": 33},
    },
    {
        "maison": "Serpentard",
        "baguette": {"bois": "ébène", "coeur": "ventricule de dragon", "longueur": 27},
    },
    {
        "maison": "Poufsouffle",
        "baguette": {"bois": "saule", "coeur": "plume de phénix", "longueur": 16},
    },
    {
        "maison": "Serdaigle",
        "baguette": {"bois": "cerisier", "coeur": "plume de phénix", "longueur": 11},
    },
    {
        "maison": "Poufsouffle",
        "baguette": {"bois": "tremble", "coeur": "plume de phénix", "longueur": 12},
    },
    {
        "maison": "Serpentard",
        "baguette": {"bois": "ébène", "coeur": "plume de serpent", "longueur": 10},
    },
    {
        "maison": "Serdaigle",
        "baguette": {"bois": "peuplier", "coeur": "corail", "longueur": 30},
    },
    {
        "maison": "Serpentard",
        "baguette": {"bois": "saule", "coeur": "plume de phénix", "longueur": 10},
    },
    {
        "maison": "Poufsouffle",
        "baguette": {"bois": "tremble", "coeur": "plume de phénix", "longueur": 12},
    },
    {
        "maison": "Poufsouffle",
        "baguette": {"bois": "pommier", "coeur": "crin de licorne", "longueur": 22},
    },
]


# Résultat attendu :
# bois_serpentard(liste_baguettes) = "ébène"
# maison_plume_phenix(liste_baguettes) = "Poufsouffle"
# maison_baguette_courte(liste_baguettes) = "Poufsouffle"


"""
Complète la fonction en conservant sa signature
"""


def bois_serpentard(liste_baguettes):
    "cette fonction renvoie une chaine de caractère"

def maison_plume_phenix(liste_baguettes):
    "cette fonction renvoie une chaine de caractère"

def maison_baguette_courte(liste_baguettes):
    "cette fonction renvoie une chaine de caractère"


### Correction

def bois_serpentard(liste_baguettes):
    count_bois = {}
    for bag in liste_baguettes:
        if bag["maison"] == "Serpentard":
            if bag["baguette"]["bois"] in count_bois:
                count_bois[bag["baguette"]["bois"]] += 1
            else:
                count_bois[bag["baguette"]["bois"]] = 1
    return max(count_bois, key=count_bois.get)


def maison_plume_phenix(liste_baguettes):
    count_maison = {}
    for bag in liste_baguettes:
        if bag["baguette"]["coeur"] == "plume de phénix":
            if bag["maison"] in count_maison:
                count_maison[bag["maison"]] += 1
            else:
                count_maison[bag["maison"]] = 1
    return max(count_maison, key=count_maison.get)


maisons_HP = ["Gryffondor", "Serdaigle", "Serpentard", "Poufsouffle"]


def maison_baguette_courte(liste_baguettes):
    moyenne = {"Gryffondor": 0, "Serdaigle": 0, "Serpentard": 0, "Poufsouffle": 0}
    compteur = {"Gryffondor": 0, "Serdaigle": 0, "Serpentard": 0, "Poufsouffle": 0}
    for bag in liste_baguettes:
        moyenne[bag["maison"]] += bag["baguette"]["longueur"]
        compteur[bag["maison"]] += 1
    for maison in maisons_HP:
        moyenne[maison] = moyenne[maison] / compteur[maison]
    return min(moyenne, key=moyenne.get)


### A la place de max(dictionnaire, key = dictionnaire.get), on peut utiliser

def maximum_count(compteur):
    max = ""
    nb_count = 0
    for key, value in compteur.items():
        if value > nb_count:
            nb_count = value
            max = key
    return max