"""
Lore :
Chaque année, une maison est attribuée aux nouveaux arrivants à Poudlard. L'affectation se détermine en fonction des caractéristiques de l'individu, bien que 
le choix final lui revienne. C'est grâce au choixpeau que la maison la plus adaptée est déterminée. 

Enoncé :
Rédige une fonction qui reproduit le comportement du choixpeau. A partir de 3 caractérisques (aptitude sportive, personnalité, couleur préférée), détermine la maison la 
plus appropriée. Les caractéristiques propres à chaque maison seront fournies.
En cas d'égalité, applique la priorité suivante : gryffondor > poufsouffle > serdaigle > serpentard.

Indice 1 : un dictionnaire est une structure pratique pour relever le nombre d'occurences
Indice 2 : les caractérisques des maisons sont contenues dans une liste. Il est possible de tirer avantage de cette structure pour simplifier le code
Indice 3 : et si tu conservais les caractéristiques du nouvel eleve dans le meme format que celui dans maison, soit une liste de 3 élément ?
Indice 4 : avec une boucle for, tu peux vérifier à quelle maison correspondent chacune des caractéristiques. En effet, grâce à l'astuce de l'indice précédent,
les mêmes caractérisques sont situés au même index dans la liste.
Indice 5 : il ne reste plus qu'à renvoyer la maison avec le plus d'occurence parmi les caractérisques fournies !
Indice 6 : attention à la priorité en cas d'égalité ! Avoir un certain ordre dans le dictionnaire permet d'éviter des complexités superflues.

"""

### Template fourni aux élèves

# Caractérisques des maisons (ne pas modifier)

gryffondor = ["athlete", "courageux", "rouge"]
poufsouffle = ["très actif", "loyal", "jaune"]
serdaigle = ["paresseux", "creatif", "bleu"]
serpentard = ["actif", "tricheur", "vert"]


"""
Complète la fonction en conservant sa signature
"""


def choixpeau(sport, caractere, couleur):
    "cette fonction renvoie une chaine de caractère parmi gryffondor, poufsouffle, serdaigle ou serpentard"


### Correction

def choixpeau(sport, caractere, couleur):
    tab = [sport, caractere, couleur]
    points = {
        "gryffondor": 0,
        "poufsouffle": 0,
        "serdaigle": 0,
        "serpentard": 0,
    }

    for i in range(len(tab)):
        if tab[i] == gryffondor[i]:
            points["gryffondor"] += 1
        elif tab[i] == poufsouffle[i]:
            points["poufsouffle"] += 1
        elif tab[i] == serdaigle[i]:
            points["serdaigle"] += 1
        elif tab[i] == serpentard[i]:
            points["serpentard"] += 1
        print(points)
    maximum = -1
    for cle, valeur in points.items():
        if valeur > maximum:
            maximum = valeur
            maison = cle
    return maison