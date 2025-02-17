"""
Lore :
Dolores Ombrage est la nouvelle professeure de Défense contre les Forces du Mal. Ses cours purement
théoriques reposent sur l'étude et la copie du manuel "Théorie des stratégies de défense magique" par
Wilbert Eskivdur. Pour gagner du temps, vous imaginez développer un sort permettant de recopier
autant de fois que souhaité un texte.

Enoncé :
Rédiger une procédure qui prend en entrée un texte et le nombre n de fois dont le texte doit être recopié.
La procédure affiche le texte n fois (séparé par un saut de ligne)

Indice 1 : pour faire un saut de ligne, on utilise \n
"""

### Template fourni aux élèves

texte = "La première règle de la défense magique est la préparation. Comme le dit l'adage sorcier, 'Mieux vaut prévenir que guérir'. \
    Une préparation adéquate implique une connaissance approfondie des sorts défensifs, des contre-mesures et des moyens de renforcer \
    les défenses magiques existantes. Un sorcier bien préparé est mieux équipé pour faire face aux menaces potentielles et pour réagir\
    rapidement en cas d'attaque surprise. Un autre principe fondamental de la défense magique est la concentration. En situation de crise, \
    il est essentiel de maintenir une concentration totale sur la tâche à accomplir. Les sorts de défense exigent une précision et une maîtrise \
    extrêmes, et toute distraction peut compromettre leur efficacité. Les sorciers doivent s'entraîner à maintenir leur concentration même dans \
    des conditions stressantes ou chaotiques, car cela peut faire la différence entre la victoire et la défaite"

"""
Rédige une procédure pour recopier ce texte n fois.
Garde la même signature pour la procédure !
"""


def copie(texte, n):
    "ecrit ton code ici"


### Correction


def correction_copie(texte, n):
    for i in range(n):
        print(texte)
        print("\n")
