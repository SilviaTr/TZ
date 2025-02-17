
"""
Lore :

Tony Stark, alias Iron Man, est en pleine recherche sur l'optimisation des systèmes de défense de la planète.
Cependant, il est distrait par un problème de calcul. Il doit analyser les performances d'une nouvelle technologie,
mais les résultats sont donnés sous forme de tableaux numériques, et il doit extraire des valeurs spécifiques.

Heureusement, Bruce Banner, se joint à lui pour résoudre ce problème. Ils décident de créer un programme Python qui extrairait rapidement les données dont ils ont besoin.
Tony se tourne vers ses notes de programme et pose l'énoncé suivant :

Enoncé:

À partir d'un tableau "technologie" fourni, crée un programme Python qui extrait les valeurs du premier, troisième, 23 eme element, dernier et avant-dernier élément du tableau.

Interdit : aucun

Indices 1: Utiliser les indices de position dans les listes.
Indices 2: Une boucle for peut être envisagée pour explorer d'autres approches.

"""

### Template fourni aux élèves

# Jeux de test

elements_tony_stark = ["Tony Stark", "Laboratoire Stark","Système de Défense","Technologie d'Intelligence Artificielle",
    "Tableau Numérique", "Données de Performance","Résultats de Test", "Optimisation","Bruce Banner", "Exploitation des Données",
    "Algorithmes Avancés","Extrayeur de Valeurs","Valeurs Spécifiques", "Bureau de Stark Industries", "Écran d'Affichage",
    "Calculs en Temps Réel", "Prototype de Technologie", "Analyse de Données", "Système de Surveillance", "Tableau de Bord",
    "Rapport d’Analyse","Base de Données","Vision", "Outils de Programmation","Code Python","Erreurs de Calcul",
    "Interface Utilisateur", "Feedback de Bruce", "Sécurité des Systèmes","Mise à Jour Logicielle", "Tests de Performance",
    "Rapport Visuel", "Simulation","Module de Contrôle","Analyse Prédictive","Équipe des Avengers", "Menace Potentielle",
    "Moteur d'Analyse", "Réglages Finaux", "Progrès Technologique", "Documentation","Communication","Scénario d'Urgence",
    "Nouveaux Modules","Rapport de Synthèse","Débriefing","Validation des Résultats", "Plan de Défense",
    "Cohérence des Données","Impact Global"]


# Résultat attendu :
# Premier élément : Tony Stark
# Troisième élément :Système de Défense
# Vingt-troisième élément : Vision
# L'avant-dernier élément : Cohérence des Données
# Dernier élément : Impact Global

"""
Rédige un programme pour déterminer la valeur du premier, du dernier, du troisième, du vingt-troisième élément et de l'avant-dernier élément.

/!\ Les jeux de tests te permettent de vérifier ton programme. 
Le programme solution de l'exercice doit utiliser le tableau d'entrée `notes` et avoir pour résultat les variables : 
- `premier_element`
- `troisieme_element`
- `vingt_troisieme_element`
- `avant_dernier_element`
- `dernier_element`
"""




### Correction

# Extraction des valeurs souhaitées

### Correction
def element(input):
    premier_element = input[0]  # Premier élément
    troisieme_element =input[2]  # Troisième élément
    vingt_troisieme_element =input[22]  # Vingt-troisième élément
    avant_dernier_element = input[-2]  # Avant-dernier élément
    dernier_element = input[-1]
    return [premier_element,troisieme_element,vingt_troisieme_element,avant_dernier_element,dernier_element]

output = element(elements_tony_stark)
print(output)


