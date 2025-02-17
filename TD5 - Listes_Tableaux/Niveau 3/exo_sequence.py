"""
Lore :

Dans le bureau de Tony Stark, alors qu'il s'entoure de ses meilleurs alliés, il réalise qu'il doit analyser les
interactions entre les membres de l'équipe. Pour ce faire, il compile une liste de noms représentant les personnes
présentes lors de diverses réunions.

Pour identifier à quelle fréquence certaines combinaisons de membres se retrouvent ensemble, Tony décide de rechercher
des séquences spécifiques de noms. Armé de son expertise en programmation, il écrit un programme Python pour compter
les occurrences d'une séquence de noms donnée dans sa liste.

À chaque itération, il compare des sous-listes avec la séquence cible, enregistrant le nombre d'apparitions et les
indices correspondants. Cela lui permet de mieux comprendre les dynamiques d'équipe et de préparer ses stratégies pour
de futures collaborations. En fin de compte, chaque donnée compte, et grâce à son programme, Tony peut prendre des
décisions éclairées pour maximiser l'efficacité de son équipe.

Énoncé :

Écrire un programme Python qui compte le nombre d'occurrences d'une séquence donnée de noms dans une liste principale de noms.
Le programme doit également enregistrer les positions où cette séquence apparaît.

La liste principale est liste_noms, contenant plusieurs noms.
La séquence à rechercher est spécifiée dans la liste sequence.
Le programme doit parcourir liste_noms et comparer les sous-listes correspondantes à sequence.

Conditions :
Le programme doit afficher le nombre total d'occurrences de la séquence ainsi que les indices de ces occurrences dans liste_noms.
"""

### Template fourni aux élèves

# Jeux de test
liste_noms = [
    "Tony Stark", "Pepper Potts", "James Rhodes", "Natasha Romanoff",
    "Steve Rogers", "Bruce Banner", "Clint Barton", "Wanda Maximoff",
    "Vision", "Thor", "Peter Parker", "Doctor Strange",
    "Nick Fury", "Maria Hill", "Gamora", "Drax","Tony Stark", "Natasha Romanoff",
    "Rocket", "Groot", "Shuri", "Okoye",
    "Tony Stark", "Natasha Romanoff", "Steve Rogers", "Bruce Banner",
    "Peter Parker", "Wanda Maximoff", "Thor", "James Rhodes",
    "Nick Fury", "Pepper Potts", "Clint Barton", "Doctor Strange"
]

# Création de la séquence à rechercher (par exemple, une combinaison de noms)
sequence = ["Tony Stark", "Natasha Romanoff"]
# Résultat attendu :
# La séquence apparaît 2 fois dans la liste.
# Les positions des occurrences sont : [16, 22]

#
"""
Rédige un programme Python qui compte le nombre d'occurrences d'une séquence donnée de noms dans une liste principale de noms.
Le programme doit également enregistrer les positions où cette séquence apparaît.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée liste_noms et sequence avoir pour résultat
 les variables: compteur,positions
"""
### Correction


def sequence(input):
    liste_noms=input[0]
    sequence=  input[1]
    compteur = 0
    len_sequence = len(sequence)
    positions = []  # Liste pour stocker les positions des occurrences

# Parcourir la liste principale et vérifier les sous-listes correspondantes
    for i in range(len(liste_noms) - len_sequence + 1):
        if liste_noms[i:i + len_sequence] == sequence:
            compteur += 1
            positions.append(i)  # Ajouter la position de l'occurrence
    return (compteur, positions)

output=sequence((liste_noms,sequence))

print(output)

