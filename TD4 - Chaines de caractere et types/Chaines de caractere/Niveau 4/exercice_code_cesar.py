"""
Lore :
Pendant les vacances, Harry Potter et Hermione Granger s'échangent des lettres. Pour s'assurer que leurs discussions ne soient pas interceptées, ils ont développé un code secret.
Harry nous a confié que les "a" devenait un "c" dans leur nouvel alphabet.

Enoncé :
Ecris un programme Python pour déchiffrer leurs messages. Le message déchiffré doit être contenu dans la variable message_decode.

Interdit : utilisation de la fonction replace

Indice 1 : Connais-tu le code de César ?
Indice 2 : il semblerait que chaque lettre du message doit être décalée de deux par rapport à l'alphabet
Indice 3 : pour gérer les lettres y et z, l'opérateur modulo est utile
Indice 4 : une fois l'alphabet de correspondance créé, le même code que celui de l'exercice du fourchelangue peut être utilisé

"""

### Template fourni aux élèves

message = "vw gu wp itcpf uqtekgt"
alphabet = "abcdefghijklmnopqrstuvwxyz"

"""
Rédige un programme pour déchiffre le message envoyé par Harry à Hermione.
Le programme solution de l'exercice doit bien utiliser en entrée la chaine de caractère message et avoir pour résultat la variable message_decode
"""


### Correction

alphabet_dechiffrage = ""

for i in range(len(alphabet)): #création du nouvel alphabet
    alphabet_dechiffrage = alphabet_dechiffrage + alphabet[(i+2)%26] # le chiffrage du message correspond à décaler de deux lettres de l'alphabet chaque lettre du message
for i in range(len(message)):
    if message[i] in alphabet:
        j = 0
        while message[i] != alphabet_dechiffrage[j]:
            j+=1
        message_decode = message_decode + alphabet[j]
    else:
        message_decode += message[i]
