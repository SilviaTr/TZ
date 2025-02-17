"""
Lore :
Pour préparer ton affrontement avec Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom, tu souhaites déchiffrer la
prophétie de Sibylle Trelawney. Tu te rappelles de la note de Dumbledore qui t'avait permis de récupérer une
lettre. Son utilité était donc de déchiffrer la prophétie ! Maintenant, tu as tout ce qui te faut
pour découvrir la vérité.

NB: La note de Dumbledore a été vu dans l'exercice "Message Ordre Phenix" de niveau 1: elle a permis de récupérer la lettre "i"

Enoncé :
Rédige un programme Python qui dans une chaine de caractère remplace un caractère par un autre. 
L'utilisation de la fonction replace est interdite !

NB : Cet exercice sera utile pour l'exercice "Tranmission Prophétie" de niveau 3

Indice 1 : écris ton code de façon à ce que le caractère à remplacer et le caractère de remplacement soient des variables
Indice 2 : une boucle for te permet de parcourir la chaine de caractère, caractère par caractère
Indice 3 : pour savoir quand arrêter la boucle for, utilise la fonction len pour connaitre la longueur de la chaine de caractère.
Indice 4 : les slices sont utiles pour éviter de recréer une nouvelle chaine de caractère
"""

### Template fourni aux élèves
prophetie = "Celuw quw a le pouvowr de vawncre le Sewgneur des Ténèbres approche... wl naîtra de ceux quw l'ont par trows fows défwé, wl sera né lorsque mourra le septwème mows... et le Sewgneur des Ténèbres le marquera comme son égal maws wl aura un pouvowr que le Sewgneur des Ténèbres wgnore... et l'un devra mourwr de la mawn de l'autre car aucun d'eux ne peut vwvre tant que l'autre survwt... Celuw quw détwent le pouvowr de vawncre le Sewgneur des Ténèbres sera né lorsque mourra le septwème mows..."
lettre_a_remplacer =
lettre_de_remplacement =

### Correction
for i in range(len(texte) - 1):
    if texte[i] == lettre_a_remplacer:
        texte = texte[:i] + lettre_de_remplacement + texte[i + 1 :]



# Solution alternative (mais non recommandée)
texte_reparé = ""
i = 0
for i in range(len(texte) - 1):
    if texte[i] == lettre_a_remplacer:
        texte_reparé += lettre_de_remplacement
    else:
        texte_reparé += texte[i]


"""
Cette solution créé une nouvelle chaine de caractère. Dans l'énoncé, il était cependant inscrit qu'il fallait 
remplacer dans la chaine de caractère.
Privilégier cette fonction ou l'autre dépend du contexte d'utilisation de la fonction. Lorsqu'on
souhaite conserver le texte original la version alternative est à préconiser. Dans le cas d'une
correction de texte, il n'est pas utile d'utiliser de l'espace pour une nouvelle chaine de caractère.
"""
