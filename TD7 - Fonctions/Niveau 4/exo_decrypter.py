"""
Lore : 
Un mystérieux grimoire magique a été découvert dans les profondeurs de la bibliothèque de Poudlard. 
Ce grimoire renferme des sorts puissants mais codés, nécessitant une maîtrise exceptionnelle des arts magiques pour les déchiffrer. 
En tant qu'apprenti sorcier, vous avez été choisi pour percer les secrets de ce grimoire.

Enonce :

1. Définissez une fonction appelée decoder_cesar qui prend deux paramètres en entrée : 
le message codé à décoder et un décalage (nombre entier) pour la substitution. Cette fonction
doit renvoyer le message décodé en appliquant un décalage inversé par rapport au message codé. 
Par exemple, si le décalage est de 3, chaque lettre du message codé sera remplacée par la lettre 
qui se trouve trois positions avant dans l'alphabet.

2. Définissez une fonction appelée decoder_vigenere qui prend deux paramètres en entrée : 
le message codé à décoder et une clé de chiffrement (une chaîne de caractères). 
Cette fonction doit renvoyer le message décodé en appliquant la méthode de chiffrement de Vigenère. 
Pour décoder un message codé avec la méthode de Vigenère, vous devez utiliser la clé de chiffrement 
pour inverser le processus de chiffrement appliqué. Il faut soustraire les 
nombres correspondant aux lettres du message chiffré avec les nombres correspondant aux lettres de la clé de chiffrement,
en utilisant l'opération modulo 26.

3. Demandez à l'utilisateur de choisir une méthode de décodage (César ou Vigenère) 
en saisissant "C" pour César ou "V" pour Vigenère.

4. Demandez à l'utilisateur de saisir le message codé à décoder.

5. Demandez à l'utilisateur de saisir les paramètres nécessaires pour le décodage :
Pour la méthode César : le décalage utilisé pour le chiffrement.
Pour la méthode Vigenère : la clé de chiffrement utilisée.

6. Appelez la fonction appropriée en fonction du choix de l'utilisateur pour décoder le message.

7. Affichez le message décodé à l'utilisateur.


Exemple d'execution :

Choisissez une méthode de décodage :
[C] - César
[V] - Vigenère
Votre choix : V

Entrez le message codé à décoder : Gp j wr eph tlii !

Entrez la clé de chiffrement : python

Le message décodé est : Go tue le dragon !


"""

### Jeu de test
phrases_a_crypter = ["Verbum Enchantatum. Que les mots soient la loi, leur puissance forgeant la réalité à chaque syllabe prononcée.", 
                    "Illusio Aeternum. Que l'illusion devienne réalité, persistant à travers les âges, trompant même les yeux les plus avertis."]

decalage = [7, 4]

phrases_cryptee_cesar = ["Clyibt Lujohuahabt. Xbl slz tvaz zvplua sh svp, slby wbpzzhujl mvynlhua sh ynhspan e johxbl zfsshil wyvuvujnl.",
                         "Mppywms Eixivryq. Uyi p'mppywmsr hizmirri vkepmxk, tivwmwxerx b xvezivw piw dkiw, xvsqterx qlqi piw ciyb piw tpyw ezivxmw."]

cle_de_chiffrements = ["Elementalis", "Temporarius"]

phrases_cryptee_vigenere = ["Zpvnyz Xnnpsreefyz. Jup tww xsfw fhipvl pl pam, yxuc xmmdwmrpx fzzyilrf pn kgltaxr b olnjup aqpweni ckoywfgri.",
                            "Bpxjgzo Rmnwkrgb. Ele c'qfdnwudb uemqyfgi dvociko, jwkwuhhrnk f njtzqgg cej hawl, xddagaeb gzfi xtg pelf fwl txjg rvvznal."]


### Template fourni aux élèves

# Définissez la fonction decoder_cesar qui prend deux paramètres en entrée : message et decalage
def decoder_cesar(message, decalage):
    message_decode = ""
    # ...
    return message_decode

# Définissez la fonction decoder_vigenere qui prend deux paramètres en entrée : message et cle_chiffrement
def decoder_vigenere(message, cle_chiffrement):
    message_decode = ""
    # ...
    return message_decode


# Demandez à l'utilisateur de choisir une méthode de décodage (C pour César, V pour Vigenère)
# ...

# Demandez à l'utilisateur de saisir le message codé à décoder
# ...

# Si l'utilisateur a choisi la méthode César
# ...

# Si l'utilisateur a choisi la méthode Vigenère
# ...

# Si l'utilisateur n'a pas choisi une méthode valide
# ...


### Correction

# Définissez la fonction decoder_cesar qui prend deux paramètres en entrée : message et decalage
def decoder_cesar(message, decalage):
    message_decode = ""
    for char in message:
        if char.isalpha():
            decalage_modifie = decalage % 26
            if char.islower():
                char_decode = chr(((ord(char) - ord('a') - decalage_modifie) % 26) + ord('a'))
            else:
                char_decode = chr(((ord(char) - ord('A') - decalage_modifie) % 26) + ord('A'))
            message_decode += char_decode
        else:
            message_decode += char
    return message_decode

# Définissez la fonction decoder_vigenere qui prend deux paramètres en entrée : message et cle_chiffrement
def decoder_vigenere(message, cle_chiffrement):
    message_decode = ""
    cle_index = 0
    for char in message:
        if char.isalpha():
            decalage = ord(cle_chiffrement[cle_index % len(cle_chiffrement)].lower()) - ord('a')
            if char.islower():
                char_decode = chr(((ord(char) - ord('a') - decalage) % 26) + ord('a'))
            else:
                char_decode = chr(((ord(char) - ord('A') - decalage) % 26) + ord('A'))
            message_decode += char_decode
            cle_index += 1
        else:
            message_decode += char
    return message_decode


# Demandez à l'utilisateur de choisir une méthode de décodage (C pour César, V pour Vigenère)
methode = input("Choisissez une méthode de décodage :\n[C] - César\n[V] - Vigenère\nVotre choix : ")

# Demandez à l'utilisateur de saisir le message codé à décoder
message_code = input("Entrez le message codé à décoder : ")

# Si l'utilisateur a choisi la méthode César
if methode.upper() == 'C':
    # Demandez le décalage utilisé pour le chiffrement
    decalage = int(input("Entrez le décalage utilisé pour le chiffrement : "))
    # Appelez la fonction decoder_cesar avec le message codé et le décalage
    message_decode = decoder_cesar(message_code, decalage)
    # Affichez le message décodé
    print("Le message décodé est :", message_decode)

# Si l'utilisateur a choisi la méthode Vigenère
elif methode.upper() == 'V':
    # Demandez la clé de chiffrement utilisée
    cle = input("Entrez la clé de chiffrement : ")
    # Appelez la fonction decoder_vigenere avec le message codé et la clé de chiffrement
    message_decode = decoder_vigenere(message_code, cle)
    # Affichez le message décodé
    print("Le message décodé est :", message_decode)

# Si l'utilisateur n'a pas choisi une méthode valide
else:
    print("Méthode de décodage invalide. Veuillez choisir entre C et V.")
