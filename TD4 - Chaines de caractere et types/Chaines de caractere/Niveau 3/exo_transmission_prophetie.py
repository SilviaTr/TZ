"""
Lore :
Après avoir déchiffrer la prophétie, tu veux la transmettre aux autres membres de l'ordre du Phénix. Mais tu décides de chiffrer le message avec un autre stratagème.
Au lieu d'une lettre, tu veux remplacer plusieurs lettres.

NB: Le déchiffrement de la prophétie a été vue dans l'exercice "Prophétie" de niveau 2

Enoncé :
Rédige un programme Python qui dans une chaine de caractère remplace plusieurs caractère par d'autres caractères de même longueur. 
La fonction replace est interdite !

Indice 1 : le texte doit être modifié uniquement si les caractères à remplacer et ceux de remplacement sont de même longueur
Indice 2 : les slices sont utiles pour modifier le texte sans recréer une nouvelle chaine de caractère
Indice 3 : pour éviter une erreur "out of range" ainsi que pour les slices, utiliser la longueur de la chaine de caractère décrivant les caractères à remplacer
"""

### Template fourni aux élèves
prophetie = "Celui qui a le pouvoir de vaincre le Seigneur des Ténèbres approche... il naîtra de ceux qui l'ont par trois fois défié, il sera né lorsque mourra le septième mois... et le Seigneur des Ténèbres le marquera comme son égal mais il aura un pouvoir que le Seigneur des Ténèbres ignore... et l'un devra mourir de la main de l'autre car aucun d'eux ne peut vivre tant que l'autre survit... Celui qui détient le pouvoir de vaincre le Seigneur des Ténèbres sera né lorsque mourra le septième mois..."
lettres_a_remplacer =
lettres_de_remplacement =

### Correction


if len(lettres_a_remplacer) == len(lettres_de_remplacement):
        lon = len(lettres_a_remplacer)
        for i in range(len(texte) - lon):
            if texte[i : i + lon] == lettres_a_remplacer:
                texte = texte[:i] + lettres_de_remplacement + texte[i + lon :]
