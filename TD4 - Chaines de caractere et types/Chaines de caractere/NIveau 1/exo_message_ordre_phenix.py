"""
Lore :
Dumbledore veut transmettre une information majeure à l'Ordre du Phénix. Cependant, en ces
temps sombres, il faut se méfier de tout. Ainsi, Dumbledore t'a transmis une note avec une phrase
qui te semble anodine. En te glissant le papier, il te dit "mon initiale est la clé".

Enoncé :
Rédige un programme Python qui ressort la première occurence d'un caractère dans une chaine de caractère.
Il doit renvoyer la position de la première apparition du caractère dans la chaine de caractère.
Par exemple, pour la phrase "Harry Potter et l'école des sorciers" et la lettre "y", le programme renvoie la position 5.
Si la lettre n'existe pas dans le texte ou autre cas non souhaité, le programme renvoie -1.

NB : Cet exercice sera utile pour l'exercice "Prophétie" de niveau 2

Indice 1 : écris ton code de façon à ce que le caractère à chercher soit une variable
Indice 2 : attention, en Python, les indices commence à 0. Mais on veut savoir la position du caractère dans le langage commun.
Indice 3 : on souhaite vérifier l'occurence d'un unique caractère, non de plusieurs ou d'aucun. Ajoute une vérification !
"""

### Template fourni aux élèves
"""
Rédige un programme pour corriger l'énoncé.
Le programme solution de l'exercice doit bien utiliser en entrée la chaine de caractère texte, ainsi que le caractère carac_a_trouver et avoir pour résultat la variable i qui correspond à la position de carac_a_trouver dans texte
"""

texte = "Les sorcières et les sorciers regardaient avec étonnement l'imposant château de Poudlard, ignorant les dangers qui les attendaient à l'intérieur."
carac_a_trouver = 

### Correction


if len(caractere) > 1 or len(caractere) == 0:
    i = -1
else:
    found = False
    i = 0
    while not found and i < len(texte):
        if texte[i] == caractere:
            found = True
        else:
            i += 1
    if not found:
        i = -1
    else:
        i += 1
