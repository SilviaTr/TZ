"""
Loki a saboté l'énoncé de l'examen des Avengers ! Pour pouvoir valider, il vous faut corriger ça.

Énoncé :
Écris un programme Python pour réparer l'énoncé. L'énoncé corrigé sera contenu dans la variable enonce_repare.

Interdit : Utilisation de la fonction reversed.

Indice 1 : On dirait que l'énoncé est inversé.
Indice 2 : Le slicing semble être une bonne piste pour ce problème.
Indice 3 : Le slicing peut aussi se faire avec des indices négatifs !

voici la structure:

def fonction (ennonce):
    
    enonce_repare = # insere ta correction ici ..
    
    return enonce_repare 



"""

### Template fourni aux élèves

enonce = ".sonahT ertnoc tnettab es aciremA niatpaC te naM norI"

# Correction de l'énoncé
enonce_repare = enonce[::-1]

print("L'énoncé corrigé est :", enonce_repare)