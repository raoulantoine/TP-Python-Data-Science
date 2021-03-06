#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
import csv
import re


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
# expression régulière qui matchera sur un nom de roi
with open('liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json') as j:
    monument = json.dumps(j, default=str)
    for row in monument:
        def isRoi(string):
        str = String
    match = re.search('Hugues|Robert|Henri|Philippe|Louis|Jean|Charles', str)
    if match:
        result = True
    else:
        result = False
    return result
    fichier = open("cible/" + row['fields']['reg'] + "/" + row['fields']
                   ['dpt_lettre'] + "/" + row['fields']['tico'] + ".txt", 'wt')
    fichier.writelines(row['fields']['reg'])
    fichier.close()
