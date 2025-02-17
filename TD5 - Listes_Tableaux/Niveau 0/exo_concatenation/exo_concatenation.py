

"""
Lore :
Ultron a rassemblé une armée et prévoit d'envoyer un ordre d'attaque contre la Terre.
Pour éviter d'être intercepté par les Avengers, il a segmenté l'ordre en fragments éparpillés dans une liste de chaînes de caractères.
Les fragments doivent être réassemblés avant que l'ordre d'attaque ne soit envoyé à ses lieutenants.
Mais pour s'assurer que les héros ne puissent pas intercepter son message, Ultron interdit l'utilisation de la méthode classique join().
Les fragments doivent être concaténés manuellement, un par un, dans un seul message destructeur.

Enoncé:
Écrire un programme Python qui concatène les éléments de type str dans une liste pour reformuler un texte.
Interdit : join()

Indices 1: Crée une boucle pour parcourir chaque élément de la liste.
Indices 1: Initialise un sommateur de chaînes de caractères pour accumuler les fragments du texte.


"""

### Template fourni aux élèves

# Jeux de test

# Liste initiale
ordre_attaque = [
    "L'heure", "de", "la", "destruction", "est", "venue.", "Envoyez", "toutes",
    "les", "flottes", "vers", "la", "Terre.", "Aucune", "pitié", "ne", "sera",
    "accordée.", "Notre", "armada", "écrasera", "chaque", "résistance.", "Déployez",
    "les", "vaisseaux", "sur", "les", "points", "stratégiques,", "anéantissez",
    "les", "cités", "majeures,", "et", "assurez-vous", "que", "les", "Avengers",
    "ne", "puissent", "pas", "intervenir.", "La", "planète", "doit", "tomber",
    "sous", "notre", "contrôle", "avant", "la", "fin", "du", "jour.", "Nous",
    "dominerons", "cet", "univers."
]

# Résultat attendu :
#L'heure de la destruction est venue. Envoyez toutes les flottes vers la Terre. Aucune pitié ne sera accordée.
# Notre armada écrasera chaque résistance. Déployez les vaisseaux sur les points stratégiques, anéantissez les cités majeures
# , et assurez-vous que les Avengers ne puissent pas intervenir. La planète doit tomber sous notre contrôle avant la fin du jour.
# Nous dominerons cet univers.


"""
Rédige un programme qui concatène les éléments de type str dans une liste pour reformuler un texte.

/!\ Les jeux de tests te permettent de vérifier ton programme
Le programme solution de l'exercice doit bien utiliser le tableau d'entrée "ordre_attaque" et avoir pour résultat
 les variables: ordre_attaque_conca
"""

input=ordre_attaque
### Correction

def concat(input):
    ordre_attaque_conca = ""
    for k in range(len(input)):
        if k < len(input)-1:
            ordre_attaque_conca += input[k] + " "
        else:
            ordre_attaque_conca += input[k]
    return ordre_attaque_conca
output = concat(input)

print(output)

