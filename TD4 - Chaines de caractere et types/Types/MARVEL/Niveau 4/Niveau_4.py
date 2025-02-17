"""
Lore :

Le Docteur Strange a demandé à Tony Stark de concevoir une potion permettant de neutraliser un adversaire en lui coupant temporairement ses pouvoirs. 
Tony a besoin de ton aide : il déteste les conversions et tout est indiqué en louches, alors qu'il ne dispose que d'une petite cuillère de sa cuisine !
Une louche contient l'équivalent de 6 petites cuillères.

La recette indique :

Pour 1 fiole de potion anti-pouvoir :
- 2 louches de poussière d'infini
- ½ louche d'essence de Vibranium
- ¼ louche d'extrait de Ragnarok

Tony doit convertir ces quantités en cuillères, une étape cruciale pour réussir la potion. 
Heureusement, tu lui proposes de créer une IA, le « Converto » pour l'aider à réaliser sa potion.

Niveau 4
4.1.
Modifie ton programme pour qu'il soit également possible de modifier la capacité d'une louche en petites cuillères.

4.2.
Que se passerait-il si Tony avait oublié une partie de la recette ? Peux-tu facilement modifier ton programme pour qu'il soit capable de gérer un tel cas ?
Par exemple si la recette indiquait plutôt :
----------
Pour 1 fiole de potion anti-pouvoir :
- 2 louches de poussière d'infini
- ½ louche d'essence de Vibranium
- ¼ louche d'extrait de Ragnarok
- 1 louche de fluide du Tesseract
----------
Tips : Tu peux regarder comment utiliser des listes et faire des itérations sur une liste en python.

"""

import random
from math import ceil

# jeu de données visible par l'utilisateur

# quantite_original = [2, 0.5, 0.25]
quantite_poussiere_original = 2
quantite_essence_original = 0.5
quantite_extrait_original = 0.25

# jeux de données cachés
# 4 jeux de données aléatoires de 3 éléments entre 1 et 100
jeu_de_donnees = [random.sample(range(1, 100), 3) for _ in range(4)]

# Correction

from math import ceil

""" Version sans liste : """

nbFiole = int(input("Combien de fioles souhaitez-vous confectionner ? "))
nbCuillere = int(input("Combien de petites cuillères pour une louche ? "))

text = f"Pour {nbFiole} fiole de potion anti-pouvoir :\n"
poussiere = "de poussière d'infini"
essence = "d'essence de Vibranium"
extrait = "d'extrait de Ragnarok"

quantite_poussiere_original = float(input(f"Quantité de {poussiere} (en louches) : "))
quantite_essence_original = float(input(f"Quantité de {essence} (en louches) : "))
quantite_extrait_original = float(input(f"Quantité de {extrait} (en louches) : "))

quantite_poussiere_convertie = ceil(quantite_poussiere_original * nbCuillere)
quantite_essence_convertie = ceil(quantite_essence_original * nbCuillere)
quantite_extrait_convertie = ceil(quantite_extrait_original * nbCuillere)

text += f"    - {quantite_poussiere_original * nbFiole} louches soit {quantite_poussiere_convertie * nbFiole} petites cuillères {poussiere}\n"
text += f"    - {quantite_essence_original * nbFiole} louches soit {quantite_essence_convertie * nbFiole} petites cuillères {essence}\n"
text += f"    - {quantite_extrait_original * nbFiole} louches soit {quantite_extrait_convertie * nbFiole} petites cuillères {extrait}\n"

print(text)

""" Version avec liste : 

nbFiole = int(input("Combien de fioles souhaitez-vous confectionner ? "))
nbCuillere = int(input("Combien de petites cuillères pour une louche ? "))

text = f"Pour {nbFiole} fiole de potion anti-pouvoir :\n"
ingredient = ["de poussière d'infini", "d'essence de Vibranium", "d'extrait de Ragnarok"]
quantite_convertie = [0, 0, 0]
for i in range(len(ingredient)):
    quantite_convertie[i] = ceil(quantite_original[i] * nbCuillere)
    text += f"    - {quantite_original[i] * nbFiole} louches soit {quantite_convertie[i] * nbFiole} petites cuillères {ingredient[i]}\n"

print(text)
"""
