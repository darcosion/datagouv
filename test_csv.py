# ex : python3 test_csv.py -f fr-esr-ecoles_doctorales_annuaire.csv 

import csv, argparse

parser = argparse.ArgumentParser(description="Ajout de fichier à tester")

parser.add_argument('-f', nargs=1, help='Envoie de fichiers à tester')

args = parser.parse_args()

if(args.f == None):
    print("erreur, pas de fichier à vérifier")
    quit

nbentree = 0
test = dict()

with open(args.f[0]) as csvfile:
    # le delimiter permet de définir les entrée
    # le quotechar sépare les colonnes 
    reader = csv.reader(csvfile, delimiter='\n')
    for row in list(reader)[1:]:
        trow = csv.reader(row, delimiter=';')
        test[len(list(trow)[0])] = True
        nbentree+= 1

csvfile.close()

print("Nombre d'entrée à traiter : " + str(nbentree))
if(len(test) > 1):
    print("attention, il y a {0:2d} type d'entrées, le fichier est possiblement corrompu".format(nbentree))
