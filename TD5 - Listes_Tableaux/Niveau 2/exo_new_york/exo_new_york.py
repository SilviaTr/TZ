
"""
Lore :
Une menace inattendue frappe à nouveau New York ! Un code malveillant, implanté dans les serveurs de la ville, génère des valeurs numériques erronées qui perturbent les systèmes de sécurité. Spider-Man doit intervenir, mais cette fois-ci, ses talents de programmeur seront sa seule arme.

Ta mission : créer une liste vide, puis la remplir avec une série d’entiers calculés selon la formule suivante :
𝑛+(𝑛+1)/2. Une fois la liste complétée, il faut éliminer un élément sur trois, puis retirer tous les nombres pairs,
car ils ont été corrompus par le virus.

Avec cette nouvelle liste purifiée, Spider-Man pourra restaurer l’ordre dans les serveurs de la ville !

Enoncé:

Écrire un programme Python Remplir la liste avec la formule (n + (n+1)/2) pour n allant de 1 à 100 en retirant tous les nombres paires

Interdit : numpy

Indices 1: Une boucle for ou while peuvent être envisagée.
Indices 2: initialiser une liste vide
Indices 3: utilise append()
"""

### Template fourni aux élèves

# Jeux de test

input =100
# Liste initiale

# Résultat attendu :
#[3, 5, 9, 11, 15, 17, 21, 23, 27, 29, 33, 35, 39, 41, 45, 47, 51, 53, 57, 59, 63, 65,
# 69, 71, 75, 77, 81, 83, 87, 89, 93, 95, 99, 101, 105, 107, 111, 113, 117, 119, 123,
# 125, 129, 131, 135, 137, 141, 143, 147, 149]
"""
Rédige un programme Python Remplir la liste avec la formule (n + (n+1)/2) pour n allant de 1 à 100 en retirant tous les nombres paires

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit avoir pour résultat
 les variables: L
"""
### Correction



def generate_list(input):
    L = []
    for n in range(1, input+1):
        x = int(n+ (n+1)/2)
        if x%2 !=0:
            L.append(x)
    return L

output=generate_list(input)

print(output)




