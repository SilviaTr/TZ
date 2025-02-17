"""
Lore :
Les magizoologistes sont des sorcier.e.s spécialisé.e.s dans l'étude des créatures magiques. Iels aident notamment le Département de contrôle et de régulation des créatures magiques à tenir à jour les 
classifications. Chaque sorcier.e note ses recherches sur le support de leur choix et le ministère utilise ensuite un sort pour fusionner toute la connaissance en un unique recueil.

Enoncé : 
Rédiger une fonction permettant de fusionner deux dictionnaires. Les dictionnaires ont pour clé le nom de la créature (chaine de caractère) et pour valeur son niveau de dangerosité (entier entre 1 et 5).
La fonction fusion_connaissance prend en entrée deux dictionnaires et renvoie un nouveau dictionnaire contenant les clés et les valeurs des deux dictionnaires combinés. Si une clé existe dans les deux dictionnaires, faire la moyenne de la valeur et arrondir
au plus proche pour obtenir un entier (pour des valeurs comme 1.5, on garde la valeur inférieure).


Indice 1 : pour parcourir un dictionnaire, on utilise items() avec une boucle for. Cela permet d'itérer sur chaque couple de clé et valeur.
Indice 2: l'opérateur in est utile pour parcourir le dictionnaire et vérifier la présence de la clé dans un dictionnaire
Indice 3: pour récupérer l'arrondi de la valeur, on peut utiliser la fonction round()

"""

### Template fourni aux élèves

# Jeux de test
dictionnaire1 = {
    "Horglup" : 1,
    "Fee" : 2,
    "Sphinx": 4,
    "Kelpy":4,
    "Clabbert" : 2,
    "Farfadet": 3,
    "Kappa" : 4,
    "Dragon": 5,
    "Basilic": 5,
    "Hippogriffe":2,
}

dictionnaire2 = {
    "Troll" : 4,
    "Boullu": 3,
    "Hippogriffe":3
    "Fee":4,
    "Salamandre":3,
    "Kelpy":2,
    "Noueux":3,
    "Veracrasse":1,
    "Farfadet":5,
    "Acromentule":5
}

"""
Complète la fonction en conservant sa signature
"""

def fusion_connaissance(dictionnaire1, dictionnaire2):
    # Cette fonction renvoie un dictionnaire




### Correction

def moyenne(val1, val2):
    moy = (val1 + val2) / 2
    return round(moy)


def fusion_connaissance(dictionnaire1, dictionnaire2):
    nouveau_dictionnaire = {}

    for cle, valeur in dictionnaire1.items():
        nouveau_dictionnaire[cle] = valeur

    for cle, valeur in dictionnaire2.items():
        if cle in nouveau_dictionnaire:
            nouveau_dictionnaire[cle] = moyenne(nouveau_dictionnaire[cle], valeur)
        else:
            nouveau_dictionnaire[cle] = valeur
    return nouveau_dictionnaire

