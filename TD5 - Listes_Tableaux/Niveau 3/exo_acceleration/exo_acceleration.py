"""
Lore :

Dans le laboratoire de Tony Stark, alors qu'il développe ses armures avancées, il doit comprendre les dynamiques
de mouvement pour optimiser les performances. En analysant les données de position d'un prototype,
il se retrouve avec deux listes : P, qui représente les positions, et T, qui représente les temps correspondants.

Pour garantir que son armure peut réagir rapidement aux changements de position, Tony décide de calculer les vitesses
à partir de ces données. Il écrit un programme Python pour déterminer la vitesse entre chaque position,
en prenant soin d'éviter les erreurs de division.

Une fois les vitesses calculées, il procède à une autre étape cruciale : calculer les accélérations.
Cela l'aide à comprendre comment les changements de vitesse influencent le mouvement global de l'armure.
Chaque chiffre compte dans sa quête d'innovation. En affichant la liste des accélérations, Tony s’assure que son
armure est non seulement rapide, mais aussi agile, prête à défier les plus grands adversaires.

Énoncé :

Écrire un programme Python qui calcule les vitesses et les accélérations d'un objet en mouvement à partir de deux listes : P pour les positions et T pour les temps.

La liste P contient les positions successives de l'objet.
La liste T contient les temps correspondants pour chaque position.
Le programme doit d'abord calculer les vitesses entre chaque point de position, puis utiliser ces vitesses pour calculer les accélérations.

Indice : append()

Conditions :

Évitez la division par zéro lors des calculs.
Les résultats des accélérations doivent être stockés dans une liste et affichés.

"""

### Template fourni aux élèves

# Jeux de test
P = [1, 10, 20, 15, 17, 18, 20, 35, 36, 38, 39, 40, 40, 45]
T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Résultat attendu : accelerations = []

#
"""
Rédige un programme Python qui calcule les vitesses et les accélérations d'un objet en mouvement à partir 
de deux listes : P pour les positions et T pour les temps.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée P et T avoir pour résultat
 les variables: accelerations
"""
### Correction

def velo_acc(input):
    P=input[0]
    T = input[1]
    velocities = []
    for i in range(1, len(P)):
        delta_P = P[i] - P[i - 1]  # Différence de position
        delta_T = T[i] - T[i - 1]  # Différence de temps
        if delta_T != 0:  # Éviter la division par zéro
            velocity = delta_P / delta_T
            velocities.append(velocity)


    accelerations = []
    for i in range(1, len(velocities)):
        delta_V = velocities[i] - velocities[i - 1]  # Différence de vitesse
        delta_T = T[i + 1] - T[i]  # Différence de temps
        if delta_T != 0:  # Éviter la division par zéro
            acceleration = delta_V / delta_T
            accelerations.append(acceleration)

    return [velocities, accelerations]



output=velo_acc((P,T))
print(output)
