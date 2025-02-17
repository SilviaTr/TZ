"""
Lore : 
Un mystérieux grimoire magique a été découvert dans les profondeurs de la bibliothèque de Poudlard. 
Ce grimoire renferme des sorts puissants mais codés, nécessitant une maîtrise exceptionnelle des arts magiques pour les déchiffrer. 
En tant qu'apprenti sorcier, vous avez été choisi pour percer les secrets de ce grimoire.

Enonce :

Créer un programme Python qui utilise deux méthodes de chiffrement différentes : 
le chiffrement César et le chiffrement Vigenère. Ces méthodes permettent de crypter un message en 
le déplaçant dans l'alphabet selon un décalage ou en utilisant un mot-clé pour effectuer une substitution.


1. Définissez une fonction appelée crypter_cesar qui prend deux paramètres en entrée : le message à crypter et un décalage pour la substitution.

2. Définissez une fonction appelée crypter_vigenere qui prend deux paramètres en entrée : le message à crypter et une clé de chiffrement.

3. Demandez à l'utilisateur de saisir un message à crypter.

4. Demandez à l'utilisateur de choisir la méthode de chiffrement :
"C" pour le chiffrement César
"V" pour le chiffrement Vigenère

Si l'utilisateur choisit le chiffrement César :

Demandez à l'utilisateur de saisir le décalage à utiliser.
Appelez la fonction crypter_cesar avec le message et le décalage.
Affichez le message crypté.

Si l'utilisateur choisit le chiffrement Vigenère :

Demandez à l'utilisateur de saisir la clé de chiffrement à utiliser.
Appelez la fonction crypter_vigenere avec le message et la clé de chiffrement.
Affichez le message crypté.


Exemples d'executions :

Entrez le message à crypter : Bonjour les amis
Choisissez une méthode de chiffrement :
[C] - César
[V] - Vigenère
Votre choix : C
Entrez le décalage à utiliser : 3

Le message crypté est : Erqmrxu ohv dplv

ou 

Entrez le message à crypter : Bonjour les amis
Choisissez une méthode de chiffrement :
[C] - César
[V] - Vigenère
Votre choix : V
Entrez la clé de chiffrement à utiliser : python

Le message crypté est : Rlpfnns vho puvj


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

# Définissez la fonction crypter_cesar qui prend deux paramètres en entrée : message et decalage
def crypter_cesar(message, decalage):
    message_crypte = ""
    # ...
    return message_crypte

# Définissez la fonction crypter_vigenere qui prend deux paramètres en entrée : message et cle_chiffrement
def crypter_vigenere(message, cle_chiffrement):
    message_crypte = ""
    # ...
    return message_crypte


# Demandez à l'utilisateur de saisir un message à crypter
# ...

# Demandez à l'utilisateur de choisir la méthode de chiffrement (C pour César, V pour Vigenère)
# ...

# Si l'utilisateur a choisi la méthode César
# ...

# Si l'utilisateur a choisi la méthode Vigenère
# ...

# Si l'utilisateur n'a pas choisi une méthode valide
# ...


### Correction

# Définissez la fonction crypter_cesar qui prend deux paramètres en entrée : message et decalage
def crypter_cesar(message, decalage):
    message_crypte = ""
    for char in message:
        if char.isalpha():
            decalage_modifie = decalage % 26
            if char.islower():
                char_crypte = chr(((ord(char) - ord('a') + decalage_modifie) % 26) + ord('a'))
            else:
                char_crypte = chr(((ord(char) - ord('A') + decalage_modifie) % 26) + ord('A'))
            message_crypte += char_crypte
        else:
            message_crypte += char
    return message_crypte

# Définissez la fonction crypter_vigenere qui prend deux paramètres en entrée : message et cle_chiffrement
def crypter_vigenere(message, cle_chiffrement):
    message_crypte = ""
    cle_index = 0
    for char in message:
        if char.isalpha():
            decalage = ord(cle_chiffrement[cle_index % len(cle_chiffrement)].lower()) - ord('a')
            if char.islower():
                char_crypte = chr(((ord(char) - ord('a') + decalage) % 26) + ord('a'))
            else:
                char_crypte = chr(((ord(char) - ord('A') + decalage) % 26) + ord('A'))
            message_crypte += char_crypte
            cle_index += 1
        else:
            message_crypte += char
    return message_crypte


# Demandez à l'utilisateur de saisir un message à crypter
message = input("Entrez le message à crypter : ")

# Demandez à l'utilisateur de choisir la méthode de chiffrement (C pour César, V pour Vigenère)
methode = input("Choisissez une méthode de chiffrement :\n[C] - César\n[V] - Vigenère\nVotre choix : ")

# Si l'utilisateur a choisi la méthode César
if methode.upper() == 'C':
    # Demandez le décalage à utiliser
    decalage = int(input("Entrez le décalage à utiliser : "))
    # Appelez la fonction crypter_cesar avec le message et le décalage
    message_crypte = crypter_cesar(message, decalage)
    # Affichez le message crypté
    print("Le message crypté est :", message_crypte)

# Si l'utilisateur a choisi la méthode Vigenère
elif methode.upper() == 'V':
    # Demandez la clé de chiffrement à utiliser
    cle = input("Entrez la clé de chiffrement à utiliser : ")
    # Appelez la fonction crypter_vigenere avec le message et la clé de chiffrement
    message_crypte = crypter_vigenere(message, cle)
    # Affichez le message crypté
    print("Le message crypté est :", message_crypte)

# Si l'utilisateur n'a pas choisi une méthode valide
else:
    print("Méthode de chiffrement invalide. Veuillez choisir entre C et V.")
