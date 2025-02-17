import random
from math import ceil
'''
# Lore :
Le professeur Stark a demandé à ses Avengers de travailler à la confection d'une potion donnant des pouvoirs incroyables.
Ils doivent convertir les quantités de l'ingrédient en petites cuillères, car ils n'ont qu'une petite cuillère à leur disposition !
Une louche contient l'équivalent de 6 petites cuillères.

Le programme doit retourner une chaîne de caractères de la forme :

Pour 1 fiole de potion silencieuse :\n
-	12 petites cuillères de sève du Tesseract\n
-	3 petites cuillères d'essence de Groot\n
-	2 petites cuillères de nectar d'Asgard

"""
'''
# Jeu de données visible par l'utilisateur

# quantite_original = [2, 0.5, 0.25]
pouvoir_tesseract = 14.2       # Sève du Tesseract
pouvoir_groot = 1.005       # Essence de Groot
pouvoir_asgardien = 120    # Nectar d'Asgard
'''
# Jeux de données cachés
# 4 jeux de données aléatoires de 3 éléments entre 1 et 100
jeu_de_donnees = [random.sample(range(1, 100), 3) for _ in range(4)]
'''
# Correction

"""
1 - Solution qui n'utilise ni liste, ni fonction : 
"""

quantite_convertie1 = ceil(pouvoir_tesseract * 6)
quantite_convertie2 = ceil(pouvoir_groot * 6)
quantite_convertie3 = ceil(pouvoir_asgardien * 6)

text = "Pour 1 fiole de potion des Avengers :\n"
text += f"    - {quantite_convertie1} petites cuillères de sève du Tesseract\n"
text += f"    - {quantite_convertie2} petites cuillères d'essence de Groot\n"
text += f"    - {quantite_convertie3} petites cuillères de nectar d'Asgard\n"


"""
2 - Solution avec une boucle avec le calcul et une concaténation, mais avec des listes :
"""

text = "Pour 1 fiole de potion des Avengers :\n"
ingredients = ["de sève du Tesseract", "d'essence de Groot", "de nectar d'Asgard"]
quantite_convertie = [0, 0, 0]
quantite_original = [pouvoir_tesseract, pouvoir_groot, pouvoir_asgardien]

for i in range(3):
    quantite_convertie[i] = ceil(quantite_original[i] * 6)
    text += f"    - {quantite_convertie[i]} petites cuillères {ingredients[i]}\n"

print(text)
