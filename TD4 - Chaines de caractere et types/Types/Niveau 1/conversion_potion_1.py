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

Niveau 1 :
Modifie ton programme qui renvoie la quantité nécessaire de nectar de tranquillité en nombre de petites cuillères, 
pour qu'elle soit cette fois arrondi au chiffre supérieur (il vaut toujours mieux en avoir trop que pas assez). Ce nombre doit être un entier.

Indice : 
Pour effectuer des opérations mathématiques de base en python, tu peux importer un module à l'aide de « from nom_du_module import nom_de_la_fonction ». 
Par exemple, le module « math » contient les fonctions « ceil » qui permet d'arrondir au chiffre supérieur, « floor » qui permet d'arrondir au chiffre supérieur, « sum », etc. 
Pour importer l'ensemble des fonctions contenue dans un module tu peux utiliser le symbole « * » à la place du nom de la fonction. 

"""
import random
from math import ceil

# jeu de données visible par l'utilisateur

nombre = 0.25

# jeu de test caché

nombre1, nombre2, nombre3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

# Correction
solution = ceil(nombre) * 6
