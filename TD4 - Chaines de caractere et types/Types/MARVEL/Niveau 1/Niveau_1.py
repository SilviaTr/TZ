"""
Lore :

Le docteur Strange a demandé à Tony Stark de travailler à la conception d'un sérum capable de neutraliser les cris destructeurs de Black Bolt. 
Tony a besoin de ton aide : bien qu'il soit un maître en technologie, il déteste les conversions, et tout est indiqué en louches alors qu'il n'a à sa disposition qu'une petite cuillère !
Une louche contient l'équivalent de 6 petites cuillères.

La recette indique :

Pour 1 dose de sérum silencieux :
- 2 louches d'extrait de voix astrale
- ½ louche d'élixir de calme cosmique
- ¼ louche de liquide d'invisibilité sonore

Tony doit convertir ces quantités en cuillères, une étape cruciale pour réussir le sérum.
Heureusement, tu proposes d'utiliser une fonction appelée "silent_mode()" pour l'aider à arrondir les doses correctement.

Niveau 1 :
Modifie ton programme pour qu'il renvoie la quantité nécessaire de liquide d'invisibilité sonore en nombre de petites cuillères, cette fois arrondi au chiffre supérieur (il vaut toujours mieux en avoir trop que pas assez). Ce nombre doit être un entier.

Indice :
Pour effectuer des opérations mathématiques de base en python, tu peux importer un module à l'aide de « from nom_du_module import nom_de_la_fonction ». 
Le module « math » contient des fonctions telles que « ceil » pour arrondir au chiffre supérieur, « floor » pour arrondir au chiffre inférieur, etc. 
Pour importer toutes les fonctions contenues dans un module, utilise le symbole « * ».
"""
import random
from math import ceil

# jeu de données visible par l'utilisateur

nombre = 0.25

# jeu de test caché

nombre1, nombre2, nombre3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

# Correction
solution = ceil(float(nombre) * 6)
