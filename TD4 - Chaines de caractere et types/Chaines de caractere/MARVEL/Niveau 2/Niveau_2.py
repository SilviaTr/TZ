"""
Lore :
Pour préparer ton affrontement avec Thanos, tu souhaites déchiffrer un message secret des Avengers. Tu te rappelles de la note laissée par Nick Fury qui t'avait permis de récupérer un symbole. Son utilité était donc de déchiffrer le message ! Maintenant, tu as tout ce qu'il te faut pour découvrir la vérité.

NB : Le symbole récupéré de Nick Fury a été mentionné dans l'exercice "Message des Avengers" de niveau 1 : il t'a permis de récupérer la lettre "x".

Énoncé :
Rédige un programme Python qui remplace un caractère par un autre dans une chaîne de caractères. L'utilisation de la fonction replace est interdite !

NB : Cet exercice sera utile pour l'exercice "Transmission du Message" de niveau 3.

Indice 1 : Écris ton code de façon à ce que le caractère à remplacer et le caractère de remplacement soient des variables.
Indice 2 : Une boucle for te permet de parcourir la chaîne de caractères, caractère par caractère.
Indice 3 : Pour savoir quand arrêter la boucle for, utilise la fonction len pour connaître la longueur de la chaîne de caractères.
Indice 4 : Les slices sont utiles pour éviter de recréer une nouvelle chaîne de caractères.

"""

message = "Thor, le dieu du tonnerre, s'apprête à affronter Thanos dans une bataille décisive. Les Avengers doivent unir leurs forces pour sauver l'univers."
lettre_a_remplacer = 'o'  # Exemple de caractère à remplacer
lettre_de_remplacement = '0'  # Exemple de caractère de remplacement

# Remplacement des caractères
for i in range(len(message)):
    if message[i] == lettre_a_remplacer:
        message = message[:i] + lettre_de_remplacement + message[i + 1:]

print("Le message corrigé est :", message)

"""
Dans cet exemple, on imagine que Thor a besoin d'un message secret pour unir les Avengers contre Thanos. Le programme remplace toutes les occurrences de la lettre "o" par le chiffre "0" dans le message, tout en respectant les instructions de ne pas utiliser la fonction replace.
"""
