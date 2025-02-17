'''
Au lieu de remplacer une seule lettre, tu veux remplacer plusieurs lettres par d'autres séquences de même longueur.

#NB : Le déchiffrement du message a été vu dans l'exercice "Message des Avengers" de niveau 2.

#Enoncé : Rédige un programme Python qui remplace plusieurs caractères par d'autres caractères de même longueur dans une chaîne de caractères.
L'utilisation de la fonction replace est interdite !

#Indices : Le texte doit être modifié uniquement si les caractères à remplacer et ceux de remplacement sont de même longueur.
Les slices sont utiles pour modifier le texte sans recréer une nouvelle chaîne de caractères. Pour éviter une erreur "out of range", ainsi que pour les slices, utiliser la longueur de la chaîne de caractères à remplacer.
'''

message = "Les Avengers sont en mission pour récupérer les Pierres d'Infinité avant que Thanos ne les obtienne. Ils doivent s'unir pour protéger l'univers."
lettres_a_remplacer = "Avengers"  # Séquence de caractères à remplacer
lettres_de_remplacement = "Guardian"  # Séquence de remplacement de même longueur

# Vérification de la longueur des deux chaînes
if len(lettres_a_remplacer) == len(lettres_de_remplacement):
    lon = len(lettres_a_remplacer)
    for i in range(len(message) - lon + 1):
        if message[i : i + lon] == lettres_a_remplacer:
            message = message[:i] + lettres_de_remplacement + message[i + lon:]

print("Le message chiffré est :", message)