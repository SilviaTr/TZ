"""
Lore :
Dans son atelier, Tony Stark se prépare à ajuster l’énergie de son armure pour une mission imminente.
Chaque module énergétique est représenté par une matrice, et l’énergie requise pour chaque système par un vecteur.
Pour équilibrer l’armure, il doit calculer le produit de cette matrice et du vecteur, afin d’optimiser la distribution de puissance.

Assis devant son écran, Tony tape rapidement un programme Python pour effectuer ce calcul complexe.
Chaque ligne de la matrice interagit avec le vecteur pour générer un nouveau résultat, essentiel pour maintenir la performance maximale de l'armure.
Une fois le calcul terminé, il a l’assurance que son armure est prête à affronter n’importe quel danger.

Énoncé
Écrire un programme Python qui réalise le produit d'une matrice par un vecteur.
La matrice est représentée sous la forme d'une liste de listes, où chaque sous-liste représente une ligne de la matrice.
Le vecteur est une liste simple. Le programme doit calculer le produit de chaque ligne de la matrice par le vecteur et retourner le résultat sous forme d'une liste (vecteur résultant).

Interdit : L'utilisation de bibliothèques externes comme numpy.

Indice 1 : Utilisez une double boucle for pour parcourir la matrice et effectuer la multiplication ligne par ligne.

Indice 2 : N'oubliez pas d'initialiser une liste vide pour stocker le résultat du produit matrice-vecteur.


"""

### Template fourni aux élèves

# Jeux de test
A = [[75, 8, 73, 12, 80],
[54, 85, 69, 36, 33],
[23, 37, 61, 20, 34],
[51, 49, 75, 2, 20],
[52, 100, 51, 3, 37]]
v = [1,10,-10,5,10]
# Résultat attendu :[285, 724, 223, 1, 927]

#
"""
Rédige un programme Python qui réalise le produit d'une matrice par un vecteur.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées A et v et avoir pour résultat
 les variables: resultat
"""



def pdoduit_matrice(input):
    lignes_A = len(input[0])
    colonnes_A = len(input[0][0])
    resultat = []

    for i in range(lignes_A):
        somme = 0
        for j in range(colonnes_A):
            somme += input[0][i][j] * input[1][j]
        resultat.append(somme)
    return resultat

output = pdoduit_matrice((A,v))
print(output)





