import re
import csv
import os
import json

with open('departements-france.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # creation des dossiers Region
        if not os.path.exists("cible/"+row['nom_region']):
            os.makedirs("cible/"+row['nom_region'])
            print("create folder " + row['nom_region'])

        # création des dossiers département dans les dossiers region
        if not os.path.exists("cible/"+row['nom_region']+"/"+row['nom_departement']):
            os.makedirs("cible/"+row['nom_region']+"/"+row['nom_departement'])
            print("create folder " + row['nom_departement'] + " create in " +
                  row['nom_region'])


# creation des fiches monuments
with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json') as j:
    monument = json.load(j)
    for row in monument:
        fichier = open("cible/" + row['fields']['reg'] + "/" + row['fields']
                       ['dpt_lettre'] + "/" + row['fields']['tico'] + ".txt", 'wt')
        fichier.writelines(row['fields']['reg'])
        fichier.close()
