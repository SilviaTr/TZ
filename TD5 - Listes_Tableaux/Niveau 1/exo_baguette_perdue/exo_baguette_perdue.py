"""
Lore :
Ron a perdu sa baguette. Pour l'aider dans ses recherches, il utilise un sort qui l'informe si la baguette est présente dans la piece.

Enoncé :
Le tableau piece contient les objets présents dans la pièce, sous forme de chaines de caractère.
Rédige un programme Python qui à partir de ce tableau détermine si la baguette est dans la pièce ou non. Le résultat est un booléen contenu dans la variable baguette.

Interdit : vérifier qu'il n'y a pas des boucles for avec des break
Interdire l'utilisation de in

Indice 1 : il faut utiliser une boucle pour parcourir le tableau. Est-il nécessaire de parcourir le tableau en intégralité dans tous les cas ?
Indice 2 : une boucle while permet de parcourir le tableau tant que la baguette n'a pas été trouvée
"""


### Template fourni aux élèves

# Jeux de test
piece1 = ["armoire", "chapeau", "grimoire", "baguette", "lit", "valise"]    # Résultat attendu: baguette = True
piece2 = ["baguettes", "bureau", "plume", "plante", "etagere"]                # Résultat attendu: baguette = False
piece3 = ["chaudron", "potion", "boule de cristal", "fiole", "bois", "cage", "tabouret"]     # Résultat attendu: baguette = False

"""
Rédige un programme pour déterminer si le tableau piece contient l'élément "baguette"

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée piece et avoir pour résultat la variable baguette
"""


### Correction

indice_piece = 0
baguette = False
while indice_piece < len(piece) and not baguette:
    if piece[indice_piece] == "baguette":
        baguette = True
    indice_piece += 1