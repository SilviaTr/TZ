"""
Lore :
Un mystérieux grimoire magique a été découvert dans les profondeurs de la bibliothèque de Poudlard. 
Ce grimoire renferme des sorts puissants mais codés, nécessitant une maîtrise exceptionnelle des arts magiques pour les déchiffrer. 
En tant qu'apprenti sorcier, vous avez été choisi pour percer les secrets de ce grimoire. 

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

jeu_de_test = ["Au creux de la nuit, les sortilèges murmurent leurs mystères aux initiés.", 
               "Dans l'ombre des runes anciennes, réside le pouvoir oublié des temps immémoriaux.",
               "Les pages de ce grimoire renferment les enchantements perdus de jadis."
               "Sous le voile de la lune argentée, se cache la clé des portes interdites."]

### Template fourni aux élèves

def compter_mots(phrase):
    # Votre code ici
    return

def inverser_phrase(phrase):
    # Votre code ici
    return

def trouver_mots_longueur(phrase, longueur):
    # Votre code ici
    return

# Testez vos fonctions avec ces exemples
phrase_test = "initiés. aux mystères leurs murmurent sortilèges les nuit, la de creux Au"
longueur_test = 5
print(compter_mots(phrase_test))  # Attendu : 12
print(inverser_phrase(phrase_test))  # Attendu : "Au creux de la nuit, les sortilèges murmurent leurs mystères aux initiés."
print(trouver_mots_longueur(phrase_test, longueur_test))  # Attendu : ['leurs', 'nuit,', 'creux']


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


