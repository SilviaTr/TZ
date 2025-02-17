"""
Lore :

Le docteur Strange a demandé à Tony Stark de concevoir un sérum capable de neutraliser les cris assourdissants de Black Bolt, afin de rendre une mission secrète plus sécurisée. 
Tony a besoin de ton aide car, bien qu'il soit un génie de la technologie, il déteste tout ce qui touche à la chimie et aux unités de mesure, et il n'a à disposition que des petites cuillères pour doser les ingrédients !
Une louche contient l'équivalent de 6 petites cuillères.

La recette indique :

Pour 1 dose de sérum silencieux :
- 2 louches d'extrait de voix astrale
- ½ louche d'élixir de calme cosmique
- ¼ louche de liquide d'invisibilité 

Tony doit convertir ces quantités en cuillères, une étape cruciale pour réussir la potion.

Niveau 0 :
Écris un programme qui renvoie la quantité nécessaire de liquide d'invisibilité sonore en nombre de petites cuillères (ce nombre peut être décimal).
"""
import random

# jeu de données visible par l'utilisateur

nombre = 0.25

# jeu de test caché

nombre1, nombre2, nombre3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

# Correction
solution = nombre * 6
