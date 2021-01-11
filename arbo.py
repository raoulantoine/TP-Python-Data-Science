import os
import csv
with open('departements-france.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
    print(', '.join(row))
