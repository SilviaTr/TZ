"""
Lore :
Fred et Georges Weasley ont une idée pour augmenter les points reçus pour la maison Gryffondor. Ils décident d'élaborer un sort
permettant de transformer un mot en un autre. De cette manière, ils pourront changer le registre des scores de façon que les points
reçus par les SLytherin soient pour les Gryffondor.


Enoncé :
Rédige un programme Python qui dans une chaine de caractère remplace un mot par un autre
On considère que la chaine ne se termine jamais par une lettre mais par point.
La fonction replace est interdite !

Indice 1 : une boucle while est plus appropriée pour parcourir la chaine de caractère : on peut ainsi adapter l'incrémentation de l'indice
Indice 2 : si on utilise une boucle while, il faut vérifier qu'on n'accrémente pas i de façon à cause une erreur "out of range"
Indice 3 : dans l'exercice de transmission de la prophétie, on vérifiait uniquement si la chaine contenait les caractères à remplacer. Pour s'assurer qu'il s'agit bien d'un mot et non d'un mot commençant par les mêmes lettres, une condition supplémentaire est nécessaire/
Indice 4 : la fonction isalpha() permet de vérifier que le caractère (ou plusieurs) est bien une lettre (ou plusieurs). Elle peut être utilisée pour tester si c'est bien le mot qu'on cherche et non un dérivé.

"""

### Template fourni aux élèves
chaine = "10 points pour Slytherin."
mot_a_remplacer = "Slytherin"
mot_de_remplacement = "Gryffondor"

### Correction

i = 0
while i < len(chaine):
    if (
        i + len(mot_a_remplacer) <= len(chaine)                                 # vérifie qu'il reste assez de caractères pour vérifier le mot 
        and chaine[i : i + len(mot_a_remplacer)] == mot_a_remplacer             # vérifie si le mot à venir est  le mot à remplacer
        and not chaine[i + len(mot_a_remplacer)].isalpha()                      # vérifie si c'est bien le mot voulu et non un dérivé (ex: chat != chaton)
    ):
        chaine = chaine[:i] + mot_de_remplacement + chaine[i + len(mot_a_remplacer) :]
        i += len(mot_a_remplacer)
    else:
        i += 1



