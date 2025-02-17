
"""
Lore :
Dans un monde où chaque décision doit être calculée avec une précision absolue, Tony Stark fait face à un dilemme crucial.
Au milieu de son laboratoire, entouré par des hologrammes de données financières et des croquis d'armures,
il se retrouve confronté à une tâche vitale : calculer le produit exact des valeurs critiques de ses ressources énergétiques.

Deux chiffres s'affichent sur son écran : 50 et 70. Ce sont bien plus que de simples nombres pour Tony.
Ils représentent des unités d'énergie vitales, capables de déterminer si son prochain prototype d'armure pourra fonctionner ou non.
Conscient de l'importance de cette opération, il ne laisse aucune place à l'erreur.

Sans perdre une seconde, Tony commence à coder un programme Python. Son objectif ?
Multiplier ces deux valeurs pour évaluer la puissance globale dont il dispose. Alors que ses doigts dansent sur le clavier,
il sait que ce calcul, bien que simple en apparence, pourrait jouer un rôle clé dans sa prochaine bataille pour sauver le monde. Un produit, un résultat, une victoire.

Lorsque le programme s’exécute et affiche le résultat, Stark sourit. Le calcul est terminé, et une nouvelle armure attend d'être construite.

Énoncé :

Écrire un programme Python qui calcule le produit des éléments dans la liste [50, 70]. Le programme doit itérer sur la liste et multiplier les valeurs ensemble pour retourner le produit final.

Interdit : Utilisation de bibliothèques externes comme numpy ou math.prod.

Indice 1 : Une boucle for peut être utilisée pour parcourir la liste.

Indice 2 : Pensez à initialiser une variable à 1 pour stocker le produit.

"""

### Template fourni aux élèves

# Jeux de test
L = [12, 45, 78, 23, 56, 89, 34, 67, 90, 123, 234, 345, 456, 567, 678, 765, 654, 543, 432, 321, 210, 109, 98, 87, 62, 65]


# Liste initiale

# Résultat attendu : 15120560
#
"""
Rédige  un programme Python qui calcule le produit des éléments dans la liste [50, 70]. 
Le programme doit itérer sur la liste et multiplier les valeurs ensemble pour retourner le produit final.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée L et avoir pour résultat
 les variables: produit
"""
### Correction


def produit(input):
     produit = 1
     for i in input:
          if 50 <=  i <= 70 :
               produit *= i
     return produit

output = produit(L)

print(output)
