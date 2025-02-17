"""
Lore :
Les résultats du tournoi de Quiddich sont tombés. Qui a gagné le tournoi ? Qui a récolté le plus de points ?

Enoncé :
Le score des matchs sont regroupés au sein d'une matrice 4x4.
Chaque ligne et chaque colonne décrivent une équipe dans l'ordre : Griffondor, Poufsouffle, Serdaigle, Serpentard. La case [i][j] contient le score de l'équipe i lors de son match contre l'équipe j.
Pour les cellules correspondant à un match de la même équipe (Griffondor contre Griffondor par exemple), la valeur 0 est présente pour symboliser qu'une équipe ne peut pas s'affronter elle-même.

Exemple:
score1 = [
    [0, 70, 90, 80],
    [20, 0, 70, 0],
    [70, 50, 0, 90],
    [60, 100, 90, 0],
]
Le score du match Griffondor contre Poufsouffle est de 70 contre 20 pour Grifffondor. Celui de Griffondor contre Serdaigle est de 90 contre 70 pour Griffondor.

Ecrire un programme Python pour déterminer le(s) gagnants du tournoi, c'est-à-dire celui qui a gagné le plus de matchs. Une égalité de points est considérée comme une défaite pour les deux équipes.
Le résultat attendue est une liste gagnant (en cas d'égalité du nombre de victoire, elle peut contenir plusieurs maisons). La liste gagnant contient le nom des maisons gagnantes (chaines de caractères).

Indice 1: en premier lieu, il faut compter le nombre de victoires de chacune des maisons.
Indice 2: si le score de l'EquipeA est dans la case score[i][j] alors le score de l'EquipeB est dans le case[j][i]
Indice 3: attention à l'énoncé, une égalité est considérée comme une défaite pour les deux équipes. De plus, il peut y avoir plusieurs vainqueurs. Est-ce que tu as pensé à tous les cas ?

"""

### Template fourni aux élèves

# Jeux de test

score1 = [
    [0, 170, 190, 180],
    [20, 0, 170, 30],
    [70, 50, 0, 190],
    [90, 200, 100, 0],
]
# Résultat attendu: gagnant = ["Griffondor"]

score2 = [
    [0, 170, 130, 90],
    [60, 0, 30, 0],
    [140, 60, 0, 50],
    [220, 160, 140, 0],
]
# Résultat attendu: gagnant = ["Serpentard"]

score3 = [
    [0, 210, 160, 190],
    [70, 0, 130, 40],
    [170, 160, 0, 150],
    [170, 200, 190, 0],
]
# Résultat attendu: gagnant = ["Griffondor", "Serdaigle", "Serpentard"]


correspondance_maison = ["Griffondor", "Poufsouffle", "Serdaigle", "Serpentard"]

"""
Rédige un programme pour déterminer le(s) gagnant(s) du tournoi de Quiddich à partir du tableau score.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableaux d'entrée score et avoir pour résultat le tableau gagnant.
"""


### Correction

nb_maison = len(score)

nb_victoires = [0, 0, 0, 0] # Ce tableau comptabilisera le nombre de victoires de chaque maison

# Boucle pour calculer le nombre des victoires des maisons à partir du score
for maison in range(nb_maison):
    for opposant in range(0, maison):    # Car si le score de l'EquipeA est dans la case score[i][j] alors le score de l'EquipeB est dans le case[j][i]       
        if score[maison][opposant] > score[opposant][maison]:
            nb_victoires[maison] += 1
        elif score[maison][opposant] < score[opposant][maison]:     # on ne fait pas un else car on considère qu'une égalité est une défaite pour les deux équipes
            nb_victoires[opposant] += 1

max = 0
gagnant = []

# Boucle pour calculer les maisons avec le plus de victoires donc le(s) gagnante(s) du tournoi
for maison in range(nb_maison):
    if nb_victoires[maison] > max:
        max = nb_victoires[maison]
        gagnant = [correspondance_maison[maison]]
    elif nb_victoires[maison] == max:  # Cas où plusieurs maisons ont le même nombre de matchs remportés (on considère qu'il y a plusieurs gagnants)
        gagnant.append(correspondance_maison[maison])
