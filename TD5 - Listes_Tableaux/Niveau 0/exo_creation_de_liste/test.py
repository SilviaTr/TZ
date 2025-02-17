def input_function(n):
    ma_liste = []
    for i in range(1, n[0] + 1):  # n est une liste, donc on prend le premier élément
        ma_liste += [i]
    return ma_liste

# Exemple d'utilisation
print(input_function([100]))  # Génère une liste de 1 à 100
