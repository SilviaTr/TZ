"""
Lore :
Hermione a besoin de réaliser la potion du Polynectar ! A-t-elle les ingrédients nécessaires ?

Enoncé :
Deux tableaux sont fournis en entrée. Le tableau ingredients contient tous les ingrédients nécessaires pour la recette. Le tableau sac contient les ingrédients présents dans le sac d'Hermione.
Rédige un programme Python qui à partir de ces deux tableaux détermine si Hermione a bien tous les ingrédients nécessaires pour le Polynectar. Le résultat est un booléen contenu dans la variable polynectar.

Interdit : vérifier qu'il n'y a pas des boucles for avec des break

Indice 1 : est-ce que cet exercice ne vous fait pas penser à l'exercice de la baguette perdue ? Vous pouvez utiliser le même code pour déterminer si un ingrédient de la recette est bien dans le sac d'Hermione
Indice 2 : si un ingrédient n'est pas dans le sac, le résultat est forcément False
Indice 3 : deux boucles while imbriquées sont nécessaires pour résoudre cet exercice.
"""


### Template fourni aux élèves

# Jeux de test
sac1 = [
        "sangsue",
        "peau de serpent",
        "grimoire",
        "baguette",
        "poil"
        "chaudron",
    ]
recette1 = ["sangsue", "peau de serpent", "poil"]
# Résultat attendu: polynectar = True

sac2 = [
        "sangsue",
        "grimoire",
        "baguette",
        "chaudron",
        "peau de serpent",
    ]
recette2 = ["sangsue", "peau de serpent", "poil"]

# Résultat attendu: polynectar = False

"""
Rédige un programme pour déterminer si les ingrédients dans le tableau recette sont bien tous dans le tableau sac

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableaux d'entrée recette et sac et avoir pour résultat la variable polynectar
"""


### Correction

polynectar = True
indice_recette = 0

while indice_recette < len(recette) and polynectar: # On parcourt le tableau recette tant qu'on n'a pas détecté un ingrédient manquant
    indice_sac = 0
    contenu = False
    while indice_sac < len(sac) and not contenu: # On parcourt le tableau sac tant que l'ingrédient de la recette n'a pas été trouvé dans le sac.
        if sac[indice_sac] == recette[indice_recette]:  # Ingrédient trouvé
            contenu = True                      
        indice_sac += 1
    if not contenu:                             # Ingrédient non trouvé
        polynectar = False
    indice_recette += 1
