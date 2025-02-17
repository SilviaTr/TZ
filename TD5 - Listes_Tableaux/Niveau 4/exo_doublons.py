"""
Lore : La Grande Réunion des Héros
Alors que les Avengers et les agents du S.H.I.E.L.D. se préparent à une mission décisive, Nick Fury convoque une
réunion d'urgence pour rassembler tous les héros disponibles. Il sait qu'il y a des chevauchements dans les membres des
 deux équipes, sans compter l'inclusion de Spider-Man, qui a également été sollicité. Pour s'assurer que chaque héros
 soit présent sans confusion, Tony Stark prend l'initiative de créer une liste consolidée sans doublons sans utiliser set(). Son objectif
est de compiler une liste unique des agents et des Avengers pour que personne ne manque à l'appel.

Énoncé
 Écrire un programme Python qui fusionne plusieurs listes de noms d'agents et de super-héros, en s'assurant qu'il n'y ait pas de doublons
Interdits : set.

Indices :

-Utilisez des boucles pour parcourir chaque liste.
-Vérifiez si le nom n’est pas déjà dans la liste sans doublons avant de l’ajouter.

"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
agents_shield = [
    "Nick Fury", "Phil Coulson", "Melinda May", "Clint Barton",
    "Maria Hill", "Daisy Johnson", "Jasper Sitwell", "Grant Ward",
    "Bobbi Morse", "Leo Fitz", "Jemma Simmons", "Quake",
    "Lance Hunter", "Philippa Georgiou", "Yo-Yo Rodriguez", "Frank Castle"
]

avengers = [
    "Tony Stark", "Steve Rogers", "Natasha Romanoff", "Bruce Banner",
    "Clint Barton", "Thor Odinson", "Wanda Maximoff", "Vision",
    "Black Panther", "Doctor Strange", "Hawkeye", "Spider-Man",
    "Captain Marvel", "Ant-Man", "Wasp", "Falcon",
    "Winter Soldier", "Scarlet Witch", "Hulk", "Gamora"
]

spider_man = [
    "Peter Parker", "Mary Jane Watson", "Gwen Stacy", "Aunt May",
    "Uncle Ben", "Miles Morales", "Spider-Gwen", "Venom",
    "Green Goblin", "Doctor Octopus", "Sandman", "Electro",
    "Vulture", "Kraven the Hunter", "Mysterio", "The Lizard"
]
# Résultat attendu :


# ['Nick Fury', 'Phil Coulson', 'Melinda May', 'Clint Barton', 'Maria Hill',
# 'Daisy Johnson', 'Jasper Sitwell', 'Grant Ward', 'Bobbi Morse',
# 'Leo Fitz', 'Jemma Simmons', 'Quake', 'Lance Hunter', 'Philippa Georgiou',
# 'Yo-Yo Rodriguez', 'Frank Castle', 'Tony Stark', 'Steve Rogers', 'Natasha Romanoff',
# 'Bruce Banner', 'Thor Odinson', 'Wanda Maximoff', 'Vision', 'Black Panther',
# 'Doctor Strange', 'Hawkeye', 'Spider-Man', 'Captain Marvel', 'Ant-Man', 'Wasp',
# 'Falcon', 'Winter Soldier', 'Scarlet Witch', 'Hulk', 'Gamora', 'Peter Parker',
# 'Mary Jane Watson', 'Gwen Stacy', 'Aunt May', 'Uncle Ben', 'Miles Morales',
# 'Spider-Gwen', 'Venom', 'Green Goblin', 'Doctor Octopus', 'Sandman', 'Electro',
# 'Vulture', 'Kraven the Hunter', 'Mysterio', 'The Lizard']
"""
Rédige un programme Python qui fusionne plusieurs listes de noms d'agents et de super-héros, en s'assurant 
qu'il n'y ait pas de doublons
/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée agents_shield,avengers,spider_man et avoir pour résultat
 les variables: liste_sans_doublons
"""

# correction
def sans_doublons(input):
    agents_shield=input[0]
    avengers=input[1]
    spider_man=input[2]
    liste_sans_doublons = []

    def ajouter_noms_unique(noms):
        for nom in noms:
            if nom not in liste_sans_doublons:
                liste_sans_doublons.append(nom)
    ajouter_noms_unique(agents_shield)
    ajouter_noms_unique(avengers)
    ajouter_noms_unique(spider_man)
    return liste_sans_doublons


output=sans_doublons((agents_shield,avengers,spider_man))
print(output)

