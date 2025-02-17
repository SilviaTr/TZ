"""
Lore :
C'est une nouvelle saison de Quidditch et il est l'heure de définir l'équipe Griffondor de cette année. 
Dans une équipe de Quidditch, il faut :
- 3 poursuiveurs
- 2 batteurs
- 1 gardien
- 1 attrapeur

La stratégie des Griffondors cette année est la suivante:
- pour les poursuiveurs, privilégier la précision
- pour les batteurs, privilégier la force
- pour le gardien, privilégier la réactivité
- pour l'attrapeur, privilégier la vitesse

Constituez maintenant la meilleure équipe possible pour la saison !

Enoncé :
Rédige une fonction qui prend en entrée une liste de dictionnaires correspondant aux candidats. Chaque dictionnaire décrit un individu par son nom, prénom, la position souhaitée, sa vitesse, sa précision, sa force et sa réactivité.
Cette fonction doit renvoyer une liste de 7 joueurs respectant les conditions décrites dans le lore, soit:
- 3 d'entre eux doivent avoir comme position_souhaitee poursuiveur et ils doivent s'agir de ceux avec la precision maximale parmi tous les candidats de cette position.
- 2 d'entre eux doivent avoir comme position_souhaitee batteur et ils doivent s'agir de ceux avec la force maximale parmi tous les candidats de cette position.
- 1 doit avoir comme position_souhaitee gardien et il s'agit du joueur de cette position avec la réactivité maximale.
- 1 doit avoir comme position_souhaitee attrapeur et il s'agit du joueur de cette position avec la vitesse maximale.

Indice 1 : On respecte les souhaits de position des candidats. Par conséquent, on filtre d'abord sur la position_souhaitee puis on récupère le(s) meilleur(s) dans la compétence clée parmi ceux postulant à la position
Indice 2 : Pour les poursuiveurs et les batteurs, il faut récupérer plusieurs candidats. Pour être sûr de ne pas renvoyer plusieurs fois le même, la fonction remove() peut être utile
Indice 3 : Lire la documentation de la fonction max peut vous inspirer
Indice 4 : L'argument key de la fonction max permet de préciser l'argument sur lequel on veut récupérer le maximum. Dans ce cas, comme la valeur est contenue dans un dictionnaire, une fonction lambda est pertinente pour la récupérer.


"""

### Template fourni aux élèves

# Jeux de test
candidats = [
    {
        "prenom": "Harry",
        "nom": "Potter",
        "position_souhaitee": "attrapeur",
        "vitesse": 10,
        "precision": 6,
        "force": 4,
        "reactivite": 7,
    },
    {
        "prenom": "Ronald",
        "nom": "Weasley",
        "position_souhaitee": "gardien",
        "vitesse": 5,
        "precision": 3,
        "force": 5,
        "reactivite": 8,
    },
    {
        "prenom": "Katie",
        "nom": "Bell",
        "position_souhaitee": "poursuiveur",
        "vitesse": 6,
        "precision": 7,
        "force": 2,
        "reactivite": 4,
    },
    {
        "prenom": "Angelina",
        "nom": "Johnson",
        "position_souhaitee": "poursuiveur",
        "vitesse": 8,
        "precision": 8,
        "force": 5,
        "reactivite": 2,
    },
    {
        "prenom": "Cormac",
        "nom": "McLaggen",
        "position_souhaitee": "gardien",
        "vitesse": 6,
        "precision": 4,
        "force": 6,
        "reactivite": 7,
    },
    {
        "prenom": "Jack",
        "nom": "Sloper",
        "position_souhaitee": "batteur",
        "vitesse": 3,
        "precision": 7,
        "force": 4,
        "reactivite": 5,
    },
    {
        "prenom": "Alicia",
        "nom": "Spinnet",
        "position_souhaitee": "poursuiveur",
        "vitesse": 3,
        "precision": 6,
        "force": 7,
        "reactivite": 8,
    },
    {
        "prenom": "Dean",
        "nom": "Thomas",
        "position_souhaitee": "poursuiveur",
        "vitesse": 6,
        "precision": 5,
        "force": 5,
        "reactivite": 7,
    },
    {
        "prenom": "Colin",
        "nom": "Crivey",
        "position_souhaitee": "attrapeur",
        "vitesse": 6,
        "precision": 4,
        "force": 2,
        "reactivite": 3,
    },
    {
        "prenom": "Lavande",
        "nom": "Brown",
        "position_souhaitee": "batteur",
        "vitesse": 3,
        "precision": 6,
        "force": 3,
        "reactivite": 4,
    },
    {
        "prenom": "Ritchie",
        "nom": "Coote",
        "position_souhaitee": "batteur",
        "vitesse": 4,
        "precision": 1,
        "force": 9,
        "reactivite": 5,
    },
    {
        "prenom": "Seamus",
        "nom": "Finnigan",
        "position_souhaitee": "poursuiveur",
        "vitesse": 3,
        "precision": 2,
        "force": 6,
        "reactivite": 3,
    },
    {
        "prenom": "Jimmy",
        "nom": "Peakes",
        "position_souhaitee": "batteur",
        "vitesse": 5,
        "precision": 3,
        "force": 7,
        "reactivite": 6,
    },
    {
        "prenom": "Vicky",
        "nom": "Frobisher",
        "position_souhaitee": "batteur",
        "vitesse": 4,
        "precision": 1,
        "force": 5,
        "reactivite": 5,
    },
]



"""
Complète la fonction en conservant sa signature
"""


def constituer_equipe(liste_joueurs):
    "cette fonction renvoie une liste de 7 dictionnaires"


### Correction

# Pour rendre les fonctions plus modulables, on note les informations de l'énoncé dans des variables. Si les informations changent, il suffira de modifier les variables et non les fonctions.

NB_POURSUIVEURS = 3
NB_BATTEURS = 2
NB_GARDIEN = 1
NB_ATTRAPEUR = 1


competences = {
    "poursuiveur": "precision",
    "batteur": "force",
    "gardien": "reactivite",
    "attrapeur": "vitesse",
}

# Cette fonction permet d'isoler les joueurs voulant une certaine position
def joueurs_position(liste_joueurs, position):
    joueurs_pos = []
    for joueur in liste_joueurs:
        if joueur["position_souhaitee"] == position:
            joueurs_pos.append(joueur)
    return joueurs_pos

# Cette fonction permet de récupérer le bon nombre de joueurs pour l'équipe en fonction d'une certaine competence
def max_joueurs(liste_joueurs, competence, nb_joueurs):
    titulaires = []
    for i in range(nb_joueurs):
        meilleur_joueur = max(liste_joueurs, key=lambda x: x[competence]) # Pour la fonction max, key permet de précision l'argument dont on souhaite tirer le maximum. Ici, on utiliser une lambda fonction pour extraire la compétence souhaitée.
        titulaires.append(meilleur_joueur)
        liste_joueurs.remove(meilleur_joueur)
    return titulaires


def constituer_equipe(liste_joueurs):
    equipe = []

    # On sélectionne les poursuiveurs
    poursuiveurs = joueurs_position(liste_joueurs, "poursuiveur")
    poursuiveurs_titulaires = max_joueurs(
        poursuiveurs, competences["poursuiveur"], NB_POURSUIVEURS
    )
    equipe += poursuiveurs_titulaires

    # On sélectionne les batteurs
    batteurs = joueurs_position(liste_joueurs, "batteur")
    batteurs_titulaires = max_joueurs(batteurs, competences["batteur"], NB_BATTEURS)
    equipe += batteurs_titulaires

    # On sélectionne le gardien
    gardien = joueurs_position(liste_joueurs, "gardien")
    gardien_titulaire = max_joueurs(gardien, competences["gardien"], NB_GARDIEN)
    equipe += gardien_titulaire

    # On sélectionne l'attrapeur
    attrapeur = joueurs_position(liste_joueurs, "attrapeur")
    attrapeur_titulaire = max_joueurs(attrapeur, competences["attrapeur"], NB_ATTRAPEUR)
    equipe += attrapeur_titulaire

    return equipe