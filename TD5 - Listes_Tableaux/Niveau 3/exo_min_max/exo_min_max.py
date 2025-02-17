"""
Lore :

Dans le laboratoire de Tony Stark, alors qu'il analyse les performances de ses prototypes,
il se rend compte qu'il doit évaluer les valeurs extrêmes de ses ressources énergétiques.
Une liste de valeurs, représentant l'énergie des différents modules, est affichée sur son écran.
Pour optimiser ses systèmes, il doit trouver le maximum et le minimum de ces valeurs.

Armé de son expertise en programmation, Tony décide d'écrire un programme Python pour effectuer ce calcul essentiel.
Chaque élément de la liste sera parcouru, permettant à Stark d'identifier rapidement les performances les plus élevées et les plus faibles de son équipement.

En ajustant ces valeurs, il pourra maximiser l’efficacité de ses armures et s’assurer qu’elles soient prêtes à affronter
les menaces. Le défi de déterminer ces extrêmes n'est pas simplement un exercice mathématique pour Tony,
mais une étape cruciale pour garantir le succès de sa mission. Chaque donnée compte dans sa quête pour sauver le monde.

Énoncé :

Écrire un programme Python qui calcule le maximum et le minimum des éléments d'une liste L contenant des nombres aléatoires.
Le programme doit parcourir la liste pour déterminer la valeur maximale et la valeur minimale.

Interdit : L'utilisation des fonctions intégrées max() et min() est interdite.

Indice 1 : Utilisez une boucle for pour parcourir la liste et comparer chaque élément.

Indice 2 : N'oubliez pas d'initialiser les variables pour stocker le maximum et le minimum en fonction de la première valeur de la liste.

"""

### Template fourni aux élèves

# Jeux de test
L = [8.5, 24.2, 48.7, 2.1, 16.3, 32.5, 60.0, 15.8, 75.4, 3.9, 21.6, 99.3, 57.8, 80.1, 45.5, 10.2, 63.7, 28.4, 39.9, 88.6, 71.2]

# Résultat attendu :Max =  99.3 et min =  2.1

#
"""
Rédige un programme Python qui calcule le maximum et le minimum des éléments d'une liste L contenant des nombres aléatoires.
Le programme doit parcourir la liste pour déterminer la valeur maximale et la valeur minimale.
/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée L et avoir pour résultat
 les variables: min, max
"""
### Correction



def min_max(input):
     max =input[0]
     min = input[0]
     for i in  input:
          if i > max :
               max = i
          else :
               if i < min :
                    min = i
     return (min, max)

output=min_max(L)