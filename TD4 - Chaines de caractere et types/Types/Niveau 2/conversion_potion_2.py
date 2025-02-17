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

Niveau 2
Écris un programme qui renvoie l'ensemble de la recette convertie en utilisant la petite cuillère comme unité de mesure. 
Le programme doit retourner une chaîne de caractères de la forme :

Pour 1 fiole de potion silencieuse :\n
-	12 petites cuillères de sève d'harmonie\n
-	3 petites cuillères d'élixir de quiétude\n
-	2 petites cuillères de nectar de tranquillité 

"""

import random
from math import ceil

# jeu de données visible par l'utilisateur

# quantite_original = [2, 0.5, 0.25]
seve = 2
elixir = 0.5
nectar = 0.25

# jeux de données cachés
# 4 jeux de données aléatoires de 3 éléments entre 1 et 100
jeu_de_donnees = [random.sample(range(1, 100), 3) for _ in range(4)]

# Correction

"""
1 - Solution qui n'utilise ni liste, ni fonction : 
"""

quantite_convertie1 = ceil(seve * 6)
quantite_convertie2 = ceil(elixir * 6)
quantite_convertie3 = ceil(nectar * 6)

text = "Pour 1 fiole de potion silencieuse :\n"
text += f"    - {quantite_convertie1} petites cuillères de sève d'harmonie\n"
text += f"    - {quantite_convertie2} petites cuillères d'élixir de quiétude\n"
text += f"    - {quantite_convertie3} petites cuillères de nectar de tranquillité\n"


"""
2 - Solution avec une boucle avec le calcul et une concaténation, mais avec des listes :


text = "Pour 1 fiole de potion silencieuse :\n"
ingredient = ["de sève d'harmonie", "d'élixir de quiétude", "de nectar de tranquillité"]
quantite_convertie = [0, 0, 0]
for i in range(3):
    quantite_convertie[i] = ceil(quantite_original[i] * 6)
    text += f"    - {quantite_convertie[i]} petites cuillères {ingredient[i]}\n"

"""

