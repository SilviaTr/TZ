"""
Lore :
Pour éviter que leurs plans ne soient découverts par les ennemis de l'Avengers, Natasha Romanoff et Nick Fury
ont développé une méthode de communication secrète. Dans leurs messages codés, une lettre est systématiquement remplacée
par une autre pour brouiller les pistes.

Enoncé :
Écrire une fonction reveler_message(message, lettre_a_remplacer, lettre_de_remplacement) qui remplace
au sein du texte toutes les lettres comme l'entrée lettre_a_remplacer par lettre_de_remplacement.
Le texte modifié est renvoyé en sortie.

Fonction interdite : replace

Indice 1 : il faut parcourir toute la chaîne de caractères du message. Une boucle à bornes définies est appropriée.
Indice 2 : les chaînes de caractères ne sont pas mutables ! Tu ne peux pas les modifier directement.
Indice 3 : Pour modifier les chaînes de caractères, on utilise la concaténation des chaînes de caractères.
Indice 4 : Pour recréer le nouveau message, on peut utiliser les slices pour changer uniquement le caractère concerné.
"""

### Template fourni aux élèves

# Jeux de test

message1 = "Tony Staxk cxée des axmures poux pxotéger le monde"
lettre_a_remplacer1 = "x"
lettre_de_remplacement1 = "r"


message2 = "Thor manie son martxau avzc une fprce divixe"
lettre_a_remplacer2 = "x"
lettre_de_remplacement2 = "e"


message3 = "Hulk kmakh tout kur son pakkage !"
lettre_a_remplacer3 = "k"
lettre_de_remplacement3 = "s"


"""
Complète la fonction
"""


def reveler_message(message, lettre_a_remplacer, lettre_de_remplacement):
    "La fonction renvoie une chaine de caractère"


### Correction

# Plusieurs façons de procéder pour créer le message décodé
# 1) on copie le message original puis on le modifie

def reveler_message(message, lettre_a_remplacer, lettre_de_remplacement):
    message_decode = message
    for i in range(len(message_decode)):
        if message_decode[i] == lettre_a_remplacer:
            message_decode = (
                message_decode[:i] + lettre_de_remplacement + message_decode[i + 1 :]
            )
    return message_decode


# 2) on le rédige lettre par lettre
def reveler_message2(message, lettre_a_remplacer, lettre_de_remplacement):
    message_decode = ""
    for i in range(len(message)):
        if message[i] == lettre_a_remplacer:
            message_decode += lettre_de_remplacement
        else:
            message_decode += message[i]
    return message_decode
