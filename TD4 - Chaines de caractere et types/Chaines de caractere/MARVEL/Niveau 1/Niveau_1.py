"""
Nick Fury veut transmettre une information importante aux Avengers. Cependant, en ces temps de crises interplanétaires, la prudence est de mise. Nick Fury te donne une note avec une phrase qui te semble anodine. En te glissant le papier, il te dit : "Mon initiale est la clé."

Énoncé :
Rédige un programme Python qui renvoie la position de la première apparition d'un caractère spécifique dans une chaîne de caractères.
Par exemple, pour la phrase "Iron Man et Captain America défendent la Terre" et le caractère "a", le programme doit renvoyer la position 8. Si le caractère n'existe pas dans le texte, le programme renvoie -1.

Indice 1 : Le caractère à rechercher doit être une variable.
Indice 2 : Les indices commencent à 0 en Python, mais on veut connaître la position du caractère dans le langage courant (commençant à 1).
Indice 3 : On doit vérifier que le caractère est unique et non vide.


"""
### Template fourni aux élèves
"""
Rédige un programme pour corriger l'énoncé.
Le programme solution de l'exercice doit bien utiliser en entrée la chaine de caractère texte, ainsi que le caractère carac_a_trouver et avoir pour résultat la variable i qui correspond à la position de carac_a_trouver dans texte
"""

texte = "Les Avengers se préparent à combattre une invasion extraterrestre menée par Thanos et ses sbires."
carac_a_trouver = 'e'  # Exemple de caractère à chercher

# Vérification du caractère
if len(carac_a_trouver) != 1:
    i = -1
else:
    found = False
    i = 0
    # Parcours du texte pour trouver la première occurrence du caractère
    while not found and i < len(texte):
        if texte[i] == carac_a_trouver:
            found = True
        else:
            i += 1
    # Si le caractère n'est pas trouvé, renvoyer -1
    if not found:
        i = -1
    else:
        i += 1  # Correction pour position humaine (commençant à 1)

print("La position du caractère est :", i)
