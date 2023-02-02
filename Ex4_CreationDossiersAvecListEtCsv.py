import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


# importez les packages os et csv #







# dans ce script vous allez faire les étapes suivantes:
#   - créez une variable qui va contenir le nom du fichier csv à lire, soit ici 'Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv'
#   - utilisez split pour obtenir le nom du ficher 
#   - utlisez find pour trouver l'index de '420'
#   - utilisez le slicing pour extraire le cours, soit les 6 caractères après le début de l'index que vous venez de trouver 
#   - utilisez find pour trouver l'index de 'gr'
#   - utilisez le slicing pour extraire le groupe, soit les 6 caractères après le début de l'index que vous venez de trouver 
#   - créez maintenant le dossier pour le cours. puis dans ce dossier le dossier pour le groupe
#   - créez une liste vide qui contiendra les noms des étudiants
#   - ouvrez le fichier en lecture avec pour delimiter le ;
#   - sautez la première ligne qui contient les en-têtes 
#   - Ajoutez les noms et prénoms des étudiants qui sont dans le fichier dans votre liste des étudiants
#   - Déplacez vous dans l'arborescence des dossiers pour aller dans le dossier du groupe que vous avez créé
#   - Finalement faites une boucle pour créer un dossier avec les noms et prénoms que vous avez dans votre liste.





