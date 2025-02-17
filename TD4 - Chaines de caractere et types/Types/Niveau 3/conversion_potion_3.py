"""
Lore :

Le professeur Rogue a demandé à Rohn de travailler à la confection d'une potion donnant le pouvoir de faire taire quiconque aurait le malheur de la boire. 
Rohn a besoin de ton aide : il a horreur des conversions, et tout est indiqué en louche alors qu'il n'a à sa disposition qu'une petite cuillère !
Une louche contient l'équivalent de 6 petites cuillères. 

La recette indique :

Pour 1 fiole de potion silencieuse :
-	2 louches de sève d'harmonie
-	½ louche d'élixir de quiétude
-	¼ louche de nectar de tranquillité

Rohn doit convertir ces quantités en cuillères, une étape cruciale pour réussir la potion. 
Heureusement tu proposes de créer un sort « le silencio » pour l'aider à réaliser sa potion.

Niveau 3
Modifie ton programme pour qu'il soit facilement possible de modifier la quantité finale de potion souhaitée en nombre de fioles,
puis affiche ensuite la recette avec les quantités originales en louche et leurs conversions en petites cuillères, sous forme d'une chaîne de caractères.

Par exemple :
----------
Combien de fioles de potion silencieuse souhaitez-vous créer ? 3

Pour 3 fioles de potion silencieuse :
- 8 louches soit 36 petites cuillères de sève d'harmonie
- 9 louches soit 22 petites cuillères d'élixir de quiétude
- 6 louches soit 12 petites cuillères de nectar de tranquillité
----------

"""

import random
from math import ceil

# jeu de données visible par l'utilisateur

# quantite_original = [2, 0.5, 0.25]
quantite_seve_original = 2
quantite_elixir_original = 0.5
quantite_nectar_original = 0.25

# jeux de données cachés
# 4 jeux de données aléatoires de 3 éléments entre 1 et 100
jeu_de_donnees = [random.sample(range(1, 100), 3) for _ in range(4)]

# Correction

""" Version sans liste : """

nbFiole = int(input("Combien de fioles souhaitez-vous confectionner ? "))

text = f"Pour {nbFiole} fiole de potion silencieuse :\n"
seve = "de sève d'harmonie"
elixir = "d'élixir de quiétude"
nectar = "de nectar de tranquillité"

quantite_seve_original = float(input(f"Quantité de {seve} (en louches) : "))
quantite_elixir_original = float(input(f"Quantité de {elixir} (en louches) : "))
quantite_nectar_original = float(input(f"Quantité de {nectar} (en louches) : "))

quantite_seve_convertie = ceil(quantite_seve_original * 6)
quantite_elixir_convertie = ceil(quantite_elixir_original * 6)
quantite_nectar_convertie = ceil(quantite_nectar_original * 6)

text += f"    - {quantite_seve_original*nbFiole} louches soit {quantite_seve_convertie*nbFiole} petites cuillères {seve}\n"
text += f"    - {quantite_elixir_original*nbFiole} louches soit {quantite_elixir_convertie*nbFiole} petites cuillères {elixir}\n"
text += f"    - {quantite_nectar_original*nbFiole} louches soit {quantite_nectar_convertie*nbFiole} petites cuillères {nectar}\n"

print(text)

""" Version avec liste : 
nbFiole = int(input("Combien de fioles souhaitez vous confectioner ? "))

text = f"Pour {nbFiole} fiole de potion silencieuse :\n"
ingredient = ["de sève d'harmonie", "d'élixir de quiétude", "de nectar de tranquillité"]
quantite_convertie = [0, 0, 0]
for i in range(3):
    quantite_convertie[i] = ceil(quantite_original[i] * 6)
    text += f"    - {quantite_original[i]*nbFiole} louches soit {quantite_convertie[i]*nbFiole} petites cuillères {ingredient[i]}\n"

print(text)
"""