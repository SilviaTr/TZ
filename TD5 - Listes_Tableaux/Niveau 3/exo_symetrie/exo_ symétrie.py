"""
Lore :

Dans le laboratoire de Tony Stark, alors qu’il peaufine ses systèmes d’armure, il se rend compte qu’un aspect essentiel
de la conception est souvent négligé : la symétrie. Pour garantir l’efficacité de ses créations, il doit s’assurer que
certaines listes de configurations sont symétriques. Cela pourrait avoir un impact direct sur l'équilibre et la performance de ses armures.

Tony se lance dans l’écriture d’un programme Python pour vérifier cette symétrie. Chaque élément de la liste doit être
comparé à son correspondant opposé. Si les deux s’avèrent identiques pour tous les indices, la liste est symétrique,
et il pourra avancer dans son processus de conception.

Avec son esprit analytique, Tony sait que même les détails apparemment simples peuvent avoir
un effet énorme sur le fonctionnement de ses innovations. En vérifiant cette symétrie, il s’assure que chaque armure
est à la fois esthétiquement plaisante et parfaitement fonctionnelle, prête à affronter tous les défis.

Énoncé :

Écrire 

Interdit : L'utilisation de la fonction intégrée reversed() ou de la méthode == pour comparer la liste à son inverse est interdite.

Indice 1 : Utilisez une boucle for pour comparer les éléments correspondants depuis le début et la fin de la liste.

Indice 2 : N'oubliez pas d'initialiser une variable pour suivre l'état de la symétrie.
"""

### Template fourni aux élèves

# Jeux de test
L = [56, 1, 21, 1, 56]
# Résultat attendu : True

#
"""
Rédige un programme Python qui vérifie si une liste L est symétrique, c'est-à-dire si elle est identique lorsqu'on la lit de gauche à droite et de droite à gauche.
 Le programme doit retourner True si la liste est symétrique et False sinon.
/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée L et avoir pour résultat
 les variables: sym
"""
### Correction


def symetrie(input):
     long = len(input)
     sym = True

     for i in range (0, long//2) :
          if input[i] !=input[len(input)-1-i] :
               sym = False
     return sym

output = symetrie(L)
print(output)
