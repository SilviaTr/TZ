

"""
Lore :
Tony Stark, en développant ses algorithmes de contrôle de vol pour ses armures, utilise le produit vectoriel pour
déterminer la direction de la force appliquée. Chaque vecteur représente une force agissant sur l'armure,
et le produit vectoriel lui permet de calculer la direction perpendiculaire à ces forces.

En utilisant cet algorithme, Tony peut ajuster les moteurs de l'armure pour répondre efficacement aux forces extérieures,
garantissant ainsi la stabilité et la maniabilité lors des vols ou des combats. Cette approche aide également
à prédire les mouvements des ennemis en fonction de leurs vecteurs de force.

Énoncé :

Écrire un programme Python qui, à partir de deux listes v1 et v2 représentant deux vecteurs en trois dimensions,
calcule le produit vectoriel de ces deux vecteurs. dim(v1)=dim(v2) = 3

Indice 1 : il est prossible de le faire sans boucle

Exigence :

Les listes doivent contenir exactement trois éléments représentant les coordonnées
des vecteurs en trois dimensions. Le programme doit afficher le produit vectoriel sous forme de vecteur.


"""

### Template fourni aux élèves

# Jeux de test


v1 = [2.0, 3.0, 4.0]

v2 = [5.0, 6.0, 7.0]

#resulat : Produit vectoriel : [-3.0, 6.0, -3.0]


"""
Rédige un programme Python qui, à partir de deux listes v1 et v2 représentant deux vecteurs en trois dimensions,
calcule le produit vectoriel de ces deux vecteurs. dim(v1)=dim(v2) = 3

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser les tableau d'entrées v1 et v2, pour résultat
 les variables: produit_vectoriel
"""

### Correction


def produit_vectoriel(input):
    v1,v2=input
    produit_vec = [
    v1[1] * v2[2] - v1[2] * v2[1],
    v1[2] * v2[0] - v1[0] * v2[2],
    v1[0] * v2[1] - v1[1] * v2[0]
    ]
    return produit_vec

output = produit_vectoriel((v1,v2))
print(output)




