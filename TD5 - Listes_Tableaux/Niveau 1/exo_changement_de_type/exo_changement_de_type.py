


"""
Lore :
Tony Stark, a récemment transféré une liste de codes vitaux pour une nouvelle technologie.
Cependant, en travaillant trop vite, il a commis une erreur en stockant certains de ces nombres sous forme de chaînes de caractères plutôt que de les garder en tant qu'entiers.
Cette erreur pourrait ralentir le système ou même provoquer une défaillance critique. Déterminé à corriger son erreur avant que ses systèmes ne tombent en panne,
Tony décide de concevoir rapidement un algorithme pour rectifier cette bavure.

Enoncé:
 Écrire un programme Python qui change la valeur des nombres sous forme de chaînes de caractères en entiers dans une liste.
 
Interdit : append(), remove(),pop(),replace()

Indices 1: Crée une boucle pour parcourir chaque élément de la liste.
Indices 2: Utilise int() pour changer de type.



"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
donnee=['196', '282', '961', '960', '51', '303', '412', '108', '714', '668', '709', '94', '414', '983', '264', '735', '111',
        '319', '319', '912', '563', '382', '506', '629', '966', '707', '89', '819', '96', '772', '879', '516', '181', '167',
        '219', '806', '893', '378', '260', '621', '731', '651', '397', '422', '633', '657', '559', '231', '887', '756']


# Résultat attendu :
#[196, 282, 961, 960, 51, 303, 412, 108, 714, 668, 709, 94, 414, 983,
# 264, 735, 111, 319, 319, 912, 563, 382, 506, 629, 966, 707, 89, 819,
# 96, 772, 879, 516, 181, 167, 219, 806, 893, 378, 260, 621, 731, 651,
# 397, 422, 633, 657, 559, 231, 887, 756]



"""
Rédige un programme Python qui change la valeur des nombres sous forme de chaînes de caractères en entiers dans une liste.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée "donnee" et avoir pour résultat
les variables: donnee
"""


### Correction
def type(input):
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

output=type(donnee)
print(output)
