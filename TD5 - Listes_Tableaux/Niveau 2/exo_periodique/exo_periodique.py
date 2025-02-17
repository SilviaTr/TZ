"""
Dans l'univers de Spider-Man, le jeune Peter Parker se retrouve souvent confronté à des choix difficiles. En tant 
qu'étudiant et super-héros, il apprend à filtrer ses priorités, à se concentrer sur ce qui est vraiment important et 
à ne pas se laisser distraire par des détails superflus. Tout comme un programme Python qui extrait des éléments selon 
des critères spécifiques, Spider-Man doit identifier les bonnes opportunités et agir en conséquence pour protéger ceux 
qu'il aime. C'est en apprenant à faire le tri parmi ses responsabilités qu'il devient un héros emblématique.

Enoncé:
Rédige un programme Python qui extrait tous les éléments dont l'index est un multiple de 3 à partir d'une liste donnée et les stocke dans une nouvelle liste.

Interdit : numpy

Indices 1: Pense à utiliser une boucle pour parcourir la liste.
Indices 2: Utilise l'opérateur `+=` pour ajouter des éléments à la nouvelle liste.

"""
### Template fourni aux élèves

# Jeux de test
# Liste initiale
liste_originale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12 , 40,30,50]



#Résultat attendu :Déterminant de la matrice : [1, 4, 7, 10, 30]



"""
Rédige un programme Python qui extrait tous les éléments dont l'index est un multiple de 3 à partir d'une liste donnée et les stocke dans une nouvelle liste.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau "liste_originale" et donnee le résultat:nouvelle_liste 
"""



#Corrrection

def periodique(input):
    nouvelle_liste = []
    for i in range(len(input)):
        if i % 3 == 0:
            nouvelle_liste += [input[i]]
    return nouvelle_liste

output=periodique(liste_originale)

print(output)

