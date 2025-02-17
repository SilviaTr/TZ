"""
Lore :
Harry Potter a découvert qu’il parlait le fourchelangue. Il nous a transmis l’alphabet correspondant à cette langue. Déchiffre la phrase de fourchelangue en français.

Enoncé :
Ecris un programme Python pour traduire la phrase du fourchelangue vers le français. La phrase traduite doit être contenue dans la variable phrase_traduite.

Interdit : utilisation de la fonction replace

Indice 1 : Il faut parcourir la chaine de caractère et remplacer chaque lettre par son équivalent en français
Indice 2 : Connaitre l'indice de position d'une lettre dans l'alphabet fourchelangue est utile
Indice 3 : A partir de l'indice de position dans l'alphabet fourchelangue, tu peux récupérer le caractère en français en utilisant le même indice dans l'alphabet français
"""

### Template fourni aux élèves

phrase_a_traduire = "y'fpmfpdn dfn nflhfpmn bekkqpxjqfl csfb kex"
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_fourchelangue = "cabdfgizxyvokpehjlnmqstrwu"

"""
Rédige un programme pour traduire le fourchelangue à partir des deux alphabets fournis.
Le programme solution de l'exercice doit bien utiliser en entrée la chaine de caractère enonce et avoir pour résultat la variable phrase_traduite
"""


### Correction


phrase_traduite=""
for i in range(len(phrase)):
    if phrase[i] in alphabet_fourchelangue:
        j = 0
        while phrase[i] != alphabet_fourchelangue[j]: # pour trouver l'indice de la lettre dans l'alphabet fourchelangue
            j+=1
        phrase_traduite = phrase_traduite + alphabet[j] # a partir de l'indice j, on récupère la lettre correspondante en français
    else:
        phrase_traduite += phrase[i]
