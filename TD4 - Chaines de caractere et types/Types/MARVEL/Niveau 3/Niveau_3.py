"""
Lore :

Le docteur Strange a demandé à Tony Stark de travailler à la confection d'un sérum permettant de neutraliser les pouvoirs destructeurs de Black Bolt. 
Tony a besoin de ton aide pour les conversions : toutes les quantités sont données en louches, alors qu'il n'a à sa disposition que des petites cuillères !
Une louche équivaut à 6 petites cuillères.

La recette indique :

Pour 1 dose de sérum neutralisateur :
- 2 louches d'extrait de voix astrale
- ½ louche d'élixir de calme cosmique
- ¼ louche de liquide d'invisibilité sonore

Tony doit convertir ces quantités en petites cuillères pour ajuster la préparation. Heureusement, tu peux créer un programme pour l'aider à réussir cette conversion.

Niveau 3
Modifie ton programme pour qu'il soit facilement possible de modifier la quantité finale de sérum souhaitée en nombre de doses,
puis affiche la recette avec les quantités originales en louches et leurs conversions en petites cuillères sous forme d'une chaîne de caractères.

Par exemple :
----------
Combien de doses de sérum neutralisateur souhaitez-vous créer ? 3

Pour 3 doses de sérum neutralisateur :
- 8 louches soit 36 petites cuillères d'extrait de voix astrale
- 1.5 louches soit 9 petites cuillères d'élixir de calme cosmique
- 0.75 louche soit 5 petites cuillères de liquide d'invisibilité sonore
----------

"""

import random
from math import ceil

# Quantités originales en louches
quantite_extrait_original = 2
quantite_elixir_original = 0.5
quantite_liquide_original = 0.25

# Conversion d'une louche en petites cuillères
CUILLERES_PAR_LOUCHE = 6

# Demande à l'utilisateur combien de doses il veut préparer
nbDoses = int(input("Combien de doses de sérum neutralisateur souhaitez-vous confectionner ? "))

# Conversion des quantités pour le nombre de doses spécifié
quantite_extrait_convertie = ceil(quantite_extrait_original * CUILLERES_PAR_LOUCHE)
quantite_elixir_convertie = ceil(quantite_elixir_original * CUILLERES_PAR_LOUCHE)
quantite_liquide_convertie = ceil(quantite_liquide_original * CUILLERES_PAR_LOUCHE)

# Texte de sortie
text = f"Pour {nbDoses} dose(s) de sérum neutralisateur :\n"
text += f"    - {quantite_extrait_original*nbDoses} louches soit {quantite_extrait_convertie*nbDoses} petites cuillères d'extrait de voix astrale\n"
text += f"    - {quantite_elixir_original*nbDoses} louches soit {quantite_elixir_convertie*nbDoses} petites cuillères d'élixir de calme cosmique\n"
text += f"    - {quantite_liquide_original*nbDoses} louches soit {quantite_liquide_convertie*nbDoses} petites cuillères de liquide d'invisibilité sonore\n"

# Affichage du résultat
print(text)
