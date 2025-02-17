
'''
Lore :
Pendant les vacances, Tony Stark et Peter Parker échangent des messages secrets pour discuter de leur prochain plan contre les ennemis de New York.
Pour s'assurer que leurs discussions ne soient pas interceptées, ils ont développé un code de chiffrement.
Tony nous a confié que chaque lettre du message est décalée de deux places dans leur nouvel alphabet.

Enoncé :
Écris un programme Python pour déchiffrer leurs messages. Le message déchiffré doit être contenu dans la variable message_decode.
le code doit prendre cette forme :
def fonction(message, alphabet):

    ''insere ton code ''
    
    return  message_decode

Interdit : utilisation de la fonction replace.

Indice 1 : Connais-tu le code de César ?
Indice 2 : Il semblerait que chaque lettre du message doit être décalée de deux par rapport à l'alphabet.
Indice 3 : Pour gérer les lettres y et z, l'opérateur modulo est utile.
Indice 4 : Une fois l'alphabet de correspondance créé, le même code que celui de l'exercice du fourchelangue peut être utilisé.

'''

# Message codé que Peter a envoyé à Tony
message = "ngu cxgpigtu xckpetqpv"

# Alphabet classique
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Variable pour contenir l'alphabet décalé de deux lettres
alphabet_dechiffrage = ""

# Création de l'alphabet décalé de 2 positions (code de César avec décalage de 2)
for i in range(len(alphabet)):
    alphabet_dechiffrage = alphabet_dechiffrage + alphabet[(i + 2) % 26]

# Variable pour contenir le message décodé
message_decode = ""

# Parcours de chaque caractère du message codé
for i in range(len(message)):
    if message[i] in alphabet_dechiffrage:
        # Trouver l'indice correspondant dans l'alphabet décalé
        j = 0
        while message[i] != alphabet_dechiffrage[j]:
            j += 1
        # Ajouter la lettre décodée à partir de l'alphabet original
        message_decode = message_decode + alphabet[j]
    else:
        # Garder les caractères spéciaux ou espaces non modifiés
        message_decode += message[i]

# Affichage du message déchiffré
print("Le message déchiffré est :", message_decode)
