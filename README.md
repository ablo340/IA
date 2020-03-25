# IA
Initiation a la programmation d'intelligence artificielle.


## WordPrediction

### Corpus_statistcs
Ce programme analyse un fichier texte et calcule le nombre d'occurence de mots dans un texte dans le but le faire le corpus de ce texte.
Le programme crée un fichier Json qui contient chaque mot et le nombre de fois que celui apparait dans le texte.

C'est une application en ligne de commande appelée avec des arguments.

> app.py [-h] [--out PATH] file

La commande de base est :

Cette commande afficher le corpus sur la sortie standard
> python app.py file

Cette commande avec la commande optionelle --out sauvegarde le corpus dans un fichier texte.
> python app.py --out <nom_fichier> file
