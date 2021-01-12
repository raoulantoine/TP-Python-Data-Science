import re
import csv
import os

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
