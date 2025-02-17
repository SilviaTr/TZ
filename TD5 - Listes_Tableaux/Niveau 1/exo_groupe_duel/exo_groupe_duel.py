"""
Lore :
Pour les duels, les professeurs ont besoin de diviser la classe en deux.

Enoncé :
Un tableau eleves est fourni contenant les noms (chaines de caracteres) des élèves de la classe. Rédige un programme Python qui a pour résultat deux tableaux groupe1 et groupe2 :
le premier contient les noms de la première moitié des élèves présents dans le tableau eleves et le second contient la deuxième moitié. Si le nombre d'élève est impair, le groupe 1 a plus d'élèves que le groupe 2.

Indice 1 : la répartition des élèves peut se faire avec des slices 
Indice 2 : il faut distinguer deux cas : le nombre d'élèves est pair et le nombre d'élèves est impair
Indice 3 : l'opérateur modulo % permet de vérifier si le nombre d'élèves est pair ou non
Indice 4 : l'opérateur division entière // permet de récupérer l'indice entier correspondant à la moitié du tableau élèves même lorsque la longueur du tableau est impair
"""

# Template fourni aux élèves

# Jeux de test
eleves1 = ["Harry", "Ron", "Hermione", "Neville"]          # Résultat attendu: groupe1 = ["Harry", "Ron"] ; groupe2 = ["Hermione", Neville]
eleves2 = ["Draco", "Pansy", "Gregory", "Vincent", "Daphne"]                    # Résultat attendu: groupe 1 = ["Draco", "Pansy", "Gregory"] ; groupe2 = ["Vincent", "Daphne"]
eleves3 = ["Luna", "Ginny", "Padma", "Seamus", "Dean", "Lavande", "Blaise", "Milicent", "Justin"]      # Résultat attendu: groupe1 =  ["Luna", "Ginny", "Padma", "Seamus", "Dean"] ; groupe2 = ["Lavande", "Blaise", "Milicent", "Justin"]

"""
Rédige un programme pour créer deux tableaux correspondant aux deux groupes des élèves créés en répartissant les élèves du tableau eleves

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée eleves et avoir pour résultat les deux variables groupe1 et groupe2
"""


# Correction

if len(eleves) % 2 == 0:
    groupe1 = eleves[: len(eleves) // 2]
    groupe2 = eleves[len(eleves) // 2 :]
else:
    groupe1 = eleves[: len(eleves) // 2 + 1]
    groupe2 = eleves[len(eleves) // 2 + 1 :]

