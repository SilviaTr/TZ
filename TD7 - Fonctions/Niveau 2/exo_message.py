"""
Lore :
Pour pouvoir communiquer des messages secrets à l'insu de la nouvelle directrice Dolores Ombrage,
l'armée de Dumbledore a mis en place un nouveau stratagème. Dans leurs messages, ils remplacent une 
lettre par une autre.

Enoncé :
Ecrire une fonction reveler_message(message, lettre_a_remplacer, lettre_de_remplacement) qui remplace
au sein du texte toutes les lettres comme l'entrée lettre_a_remplacer par lettre_de_remplacement.
Le texte modifié est renvoyé en sortie.

Fonction interdite : replace

Indice 1 : il faut parcourir toute la chaine de caractère du message. Une boucle à bornes définies est appropriée.
Indice 2 : les chaines de caractères ne sont pas mutables ! Tu ne peux pas les modifier directement.
Indice 3 : Pour modifier les chaines de caractères, on utilise la concaténation des chaines de caractère.
Indice 4 : Pour recréer le nouveau message, on peut utiliser les slices pour changer uniquement le caractère concerné.
"""

### Template fourni aux élèves

# Jeux de test

message1 = "rdv f lf sflle sur demfnde f 20h"
lettre_a_remplacer1 = "f"
lettre_de_remplacement1 = "a"
# Résultat attendu : "rdv a la salle sur demande a 20h"

message2 = "subveilleb busabd"
lettre_a_remplacer2 = "b"
lettre_de_remplacement2 = "r"
# Résultat attendu : "surveiller rusard"

message3 = "provego vovalum"
lettre_a_remplacer3 = "v"
lettre_de_remplacement3 = "t"
# Résultat attendu : "protego totalum"

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
