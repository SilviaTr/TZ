"""
Lore :

Les Avengers se réunissent pour résoudre un problème critique dans le système de communication développé par Tony Stark. 
Une erreur de codage a introduit des éléments indésirables, notamment la lettre 'c', qui perturbe l'analyse des données.
Tony, absorbé par l'amélioration de son armure, sollicite l'aide de ses coéquipiers. Natasha Romanoff propose de faire
appel à Bruce Banner pour concevoir un script Python capable d'éliminer ces éléments indésirables et de les remplacer
par la lettre 'w'. Ensemble, ils se plongent dans ce défi urgent dans le laboratoire de Stark, déterminés à optimiser 
le système avant que la prochaine menace ne se manifeste.

Enoncé:

Écrire un programme Python qui remplace toutes les occurrences de la lettre 'c' d'une liste de lettres pour la lettre 'w'.

Interdit : append(),remove()

Indices 1: Une boucle for ou while peuvent être envisagée.


"""

### Template fourni aux élèves

# Jeux de test


# Liste initiale
lettres = ['a', 'b', 'c', 'd', 'u', 'v', 'w','e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w','c', 'x', 'y', 'z', 'c','c', 'x', 'y','n', 'o', 'p']



# Résultat attendu :
#Liste après remplacement: ['a', 'b', 'w', 'd', 'u', 'v', 'w', 'e', 'f', 'g', 'h', 'i', 'j',
# 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'w', 'x', 'y', 'z', 'w', 'w', 'x', 'y', 'n', 'o', 'p']
"""
Rédige un programme pour retirer toute les lettre 'c' d'une liste et les remplaces par "w"

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée lettres et avoir pour résultat
 les variables: lettres 
"""
### Correction
# Retirer tous les éléments valant 'c'

def remplacement(input):
    for k in range(len(input)):
        if input[k] == 'c':
            input[k] = 'w'
    return input

output = remplacement(lettres)
print(output)





