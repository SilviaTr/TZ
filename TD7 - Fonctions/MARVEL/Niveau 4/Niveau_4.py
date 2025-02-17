"""
Lore :
Un artefact mystérieux a été découvert dans les archives secrètes du Sanctum Sanctorum. Ce manuscrit ancien contient des secrets puissants relatifs aux héros et vilains de l'univers Marvel. Votre tâche consiste à utiliser vos connaissances en programmation pour déchiffrer ces secrets !
Énoncé :

Écrire une fonction compter_mots(phrase) qui prend en entrée une phrase (une chaîne de caractères)
et renvoie le nombre de mots dans cette phrase. On considère qu'un mot est une séquence de caractères séparés par des espaces.

Écrire une fonction inverser_phrase(phrase) qui prend en entrée une phrase et 
renvoie cette phrase avec l'ordre des mots inversé. Par exemple, si la phrase est
"Bonjour tout le monde", la fonction devrait renvoyer "monde le tout Bonjour".

Écrire une fonction trouver_mots_longueur(phrase, longueur) qui prend en entrée une 
phrase et une longueur, et renvoie une liste de tous les mots dans la phrase ayant la longueur spécifiée.

Indices :

La méthode split() peut être utile pour diviser une phrase en mots.
Pour inverser l'ordre des mots, vous pouvez utiliser la méthode split() pour diviser la phrase en mots, 
puis utiliser l'indexation pour inverser l'ordre de la liste, et enfin utiliser la méthode join() pour reformer la phrase.
Pour filtrer les mots par longueur, vous pouvez utiliser une boucle et une condition pour vérifier la longueur de chaque mot.

"""

### Jeu de test

jeu_de_test = [
    "Iron Man et Captain America combattent ensemble contre Thanos et ses alliés.",
    "Spider-Man se bat contre Green Goblin et Doctor Octopus à New York.",
    "Thor et Hulk luttent pour sauver Asgard des griffes de Loki.",
    "Black Widow et Hawkeye sont membres des Avengers, ils affrontent Ultron.",
    "Wolverine et Deadpool sont des mutants qui combattent les ennemis de l'humanité.",
    "Captain Marvel vole à la rescousse, aidée de Rocket Raccoon et Groot."
]

### Template fourni aux élèves
"""
def compter_mots(phrase):
    # Votre code ici
    return

def inverser_phrase(phrase):
    # Votre code ici
    return

def trouver_mots_longueur(phrase, longueur):
    # Votre code ici
    return
"""
# Testez vos fonctions avec ces exemples
phrase = "Spider-Man se bat contre Green Goblin et Doctor Octopus à New York."
longueur = 5
print(compter_mots(phrase))  # Attendu : 12
print(inverser_phrase(phrase))  # Attendu : alliés. ses et Thanos contre ensemble combattent America Captain et Man Iron
print(trouver_mots_longueur(phrase, longueur))  # Attendu : ['contre', 'Thanos']

### Correction

def compter_mots(phrase):
    mots = phrase.split()
    return len(mots)

def inverser_phrase(phrase):
    mots = phrase.split()
    mots_inverse = mots[::-1]
    phrase_inverse = ' '.join(mots_inverse)
    return phrase_inverse

def trouver_mots_longueur(phrase, longueur):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) == longueur]
    return mots_filtres

