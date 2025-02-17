"""
Lore :
Dans la bibliothèque mystique de Kamar-Taj, Doctor Strange est en train de préparer ses défenses contre une menace mystique imminente.
Il a besoin de répertorier les armes et artefacts magiques associés à chaque maître des arts mystiques sous sa responsabilité.
Pour faciliter cela, il construit une matrice dans laquelle chaque ligne répertorie les héros, leurs armes et leurs artefacts.

Cependant, pour mieux organiser ses ressources, Strange doit transposer cette matrice. Cela lui permettra de voir,
pour chaque personnage, la combinaison exacte de pouvoir qu'il détient. Avec son savoir-faire en programmation,
Doctor Strange écrit un algorithme qui lui permet de rapidement réarranger les données. Grâce à cette transposition,
 il peut anticiper quelle combinaison de personnages et d'artefacts déployer pour la bataille qui s'annonce.

Chaque ligne transposée reflète une force prête à défendre la réalité contre les forces du chaos.

Énoncé :

Écrire un programme Python qui transpose une matrice contenant des personnages et des armes de l'univers de Doctor Strange.

La première ligne de la matrice contient les noms des personnages.
La deuxième ligne contient leurs armes principales.
La troisième ligne contient des artefacts magiques associés à chaque personnage.
Le programme doit transposer la matrice, c'est-à-dire que les colonnes deviennent des lignes, et les afficher.

Restriction :
Vous n'êtes pas autorisé à utiliser de bibliothèques externes (comme numpy).

"""

### Template fourni aux élèves

# Jeux de test
matrice = [
    ["Doctor Strange", "Wong", "Ancient One", "Mordo", "Kaecilius"],
    ["Eye of Agamotto", "Magic Staff", "Mirror Dimension", "Sling Ring", "Dark Magic"],
    ["Cloak of Levitation", "Scroll of Watoomb", "Book of Cagliostro", "Vaulting Boots", "Black Staff"]
]
# Résultat attendu :['Doctor Strange', 'Eye of Agamotto', 'Cloak of Levitation']
# ['Wong', 'Magic Staff', 'Scroll of Watoomb']
# ['Ancient One', 'Mirror Dimension', 'Book of Cagliostro']
# ['Mordo', 'Sling Ring', 'Vaulting Boots']
# ['Kaecilius', 'Dark Magic', 'Black Staff']
#
"""
Rédige un programme Python qui transpose une matrice contenant des personnages et des armes de l'univers de Doctor Strange.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées matrice et avoir pour résultat
 les variables: transpose
"""



### Correction

def transpose(input):
    matrice=input
    transpose = []

    for i in range(len(matrice[0])):
        new_row = []
        for j in range(len(matrice)):
            new_row.append(matrice[j][i])
        transpose.append(new_row)
    return transpose

output=transpose(matrice)

print(output)
