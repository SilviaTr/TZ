

"""
Lore :
Tony Stark, toujours à la recherche de moyens pour optimiser l'efficacité énergétique de ses armures, utilise la méthode
 du trapèze pour estimer les performances énergétiques de ses systèmes. Chaque point de la liste x correspond à un
 intervalle de temps pendant lequel l'armure est utilisée, et chaque valeur de f(x) représente l'énergie consommée par l'armure à cet instant précis.

En calculant l'intégrale approchée, Tony peut estimer l'énergie totale utilisée sur une période donnée. Grâce à cet
algorithme, il parvient à ajuster ses systèmes pour minimiser la consommation énergétique sans compromettre les performances.

Cette méthode d'intégration permet à Tony d'optimiser ses armures avant chaque mission, garantissant qu'elles
fonctionneront à pleine puissance sans gaspiller de précieuses ressources.

Chaque ligne transposée reflète une force prête à défendre la réalité contre les forces du chaos.

Énoncé :

Écrire un programme Python qui, à partir d'une liste de points x et des valeurs associées f(x), calcule l'intégrale
approchée de la fonction en utilisant la méthode du trapèze.

La méthode du trapèze consiste à diviser l'aire sous la courbe en petits trapèzes, puis à additionner leurs aires pour
obtenir une estimation de l'intégrale.

Le programme doit fonctionner pour des listes x et f(x) de longueurs quelconques, contenant des valeurs flottantes.

Exigence :

Les listes doivent être suffisamment grandes et variées, contenant des valeurs flottantes pour simuler une fonction continue.


"""

### Template fourni aux élèves

# Jeux de test
x = [0.0, 0.5, 1.2, 2.1, 3.0, 4.5, 5.8, 6.3, 7.7, 9.2]
f_x = [0.0, 0.6, 2.4, 5.9, 9.6, 14.0, 18.2, 21.5, 25.7, 30.0]

#resulat : 135.28


"""
Rédige un programme Python qui, à partir d'une liste de points x et des valeurs associées f(x), calcule l'intégrale
approchée de la fonction en utilisant la méthode du trapèze.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées x et f_x avoir pour résultat
 les variables: integral
"""



### Correction
def integral(input):
    x=input[0]
    f_x=input[1]
    int = 0.0

    for i in range(len(f_x) - 1):
        dx = x[i + 1] - x[i]
        int += (f_x[i] + f_x[i + 1]) * dx / 2
    return int

output=integral((x,f_x))
print(output)

