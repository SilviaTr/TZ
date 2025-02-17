'''
Lore :
Tony Stark a découvert un ancien langage extraterrestre utilisé par une race de Skrulls infiltrée sur Terre. 
Il nous a transmis l'alphabet correspondant à ce langage. Déchiffre la phrase en langage Skrull en français.

Enoncé :
Écris un programme Python pour traduire la phrase du langage Skrull vers le français. 
La phrase traduite doit être contenue dans la variable phrase_traduite.

Interdit : utilisation de la fonction replace

Indice 1 : Il faut parcourir la chaîne de caractères et remplacer chaque lettre par son équivalent en français.
Indice 2 : Connaître l'indice de position d'une lettre dans l'alphabet Skrull est utile.
Indice 3 : À partir de l'indice de position dans l'alphabet Skrull, tu peux récupérer le caractère en français en utilisant le même indice dans l'alphabet français.
'''

# Phrase en langage Skrull à déchiffrer
phrase_a_traduire = "Ltl Axtfutkl wfolltfm stwkl ygketl hgwk lawxtk s'wfoxtkl."

# Alphabets pour la traduction
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_skrull = "azertyuiopqsdfghjklmwxcvbn"

# Initialisation de la phrase traduite
phrase_traduite = ""

# Parcourir chaque caractère de la phrase
for i in range(len(phrase_a_traduire)):
    if phrase_a_traduire[i] in alphabet_skrull:
        # Trouver l'indice de la lettre dans l'alphabet Skrull
        j = 0
        while phrase_a_traduire[i] != alphabet_skrull[j]:
            j += 1
        # Ajouter la lettre correspondante en français
        phrase_traduite = phrase_traduite + alphabet[j]
    else:
        # Conserver les caractères qui ne sont pas dans l'alphabet (espaces, ponctuation, etc.)
        phrase_traduite += phrase_a_traduire[i]

# Affichage de la phrase traduite
print("La phrase traduite est :", phrase_traduite)
