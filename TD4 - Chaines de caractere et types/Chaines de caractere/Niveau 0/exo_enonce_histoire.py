"""
Lore :
Draco a saboté l'énoncé de l'examen d'histoire ! Pour pouvoir valider, il vous faut corriger ça.

Enoncé :
Ecris un programme Python pour reparer l'énoncé. L'énoncé corrigé sera contenu dans la variable enonce_repare

Interdit : utilisation de la fonction reversed

Indice 1 : On dirait que l'énoncé est inversé
Indice 2 : Le slicing semble être une bonne piste pour ce problème
Indice 3 : Le slicing peut aussi se faire avec des indices négatifs !
"""

### Template fourni aux élèves

enonce= "riovas ruel reugél ed te sétucésrep sreicros xua egufer nu rirffo'd tnattemrep eigam ed elocé enu rednof ed tnerèdicéd ) \
dratnepreS razalaS te elgiadreS anewoR ,elffuosfuoP agleH ,rodnoffyrG cirdoG( séuod tnemellennoitpecxe sreicros ertauQ .sudloM sémmon \
,seuqigam sriovuop ed seuvruopéd sennosrep ed trap al ed ruep ed te noisnehérpmocni'd tneiarffuos sreicros sel ,sna ellim ed sulp a y lI"\



"""
Rédige un programme pour corriger l'énoncé.
Le programme solution de l'exercice doit bien utiliser en entrée la chaine de caractère enonce et avoir pour résultat la variable enonce_repare
"""


### Correction

enonce_repare = enonce[::-1]