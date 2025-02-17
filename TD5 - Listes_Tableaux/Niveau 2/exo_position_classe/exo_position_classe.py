"""
Lore :
Les résultats de l'examen des potions est tombé. Tout le monde veut savoir sa note et où il se situe par rapport aux autres. Le professeur Rogue a affiché sur le mur
du fond de la classe les élèves ordonnés de la meilleure note à l'examen à la pire.

Enoncé :
Créer un programme donnant le rang d'un élève dans la liste ordre. SI l'èleve n'est pas dans la liste, renvoyer -1.
Interdire l'utilisation de in.

Indice 1 : il faut utiliser une boucle pour parcourir le tableau. Est-il nécessaire de parcourir le tableau en intégralité dans tous les cas ?
Indice 2 : une boucle while permet de parcourir le tableau tant que l'élève n'a pas été trouvée
Indice 3: ne pas oublier le cas où l'élève n'est pas dans la liste -> a la fin de la boucle while, il n'a toujours pas été trouvé
"""


### Template fourni aux élèves

# Jeux de test
ordre = ["Granger", "Brown", "Finnigan", "Potter", "Thomas", "Malefoy", "Londubat", "Patil", "Weasley", "Goyle", "Crabbe"]

nom_eleve1 = "Granger"          # Résultat attendu : 1
nom_eleve2 = "Potter"          # Résultat attendu : 4
nom_eleve3 = "Weasley"          # Résultat attendu : 9

"""
Rédige un programme pour déterminer l'ordre d'un élève donné

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser comme entrées le tableau ordre et la chaine de caractère nom_eleve. La sortie doit être position_eleve
"""


### Correction

position_eleve = 0
while ordre[position_eleve] != nom_eleve and position_eleve < (len(ordre) - 1):
    position_eleve += 1
if ordre[position_eleve] != nom_eleve:
    position_eleve = -1
else:
    position_eleve += 1


