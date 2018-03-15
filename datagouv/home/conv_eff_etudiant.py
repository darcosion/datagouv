import csv

from .models import EtudiantUniversite

# attention, le délimiteur est sensé être un ";" mais
# s'il y a des doubles quotes, il ne doit pas être pris en compte
# dedans...

firstline = True

compt = 0

with open('../fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public.csv') as csvfile:
    # le delimiter permet de définir les entrée
    # le quotechar sépare les colonnes
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        #print(compt)
        if(firstline):
            firstline = False
            continue
        trow = list(csv.reader(row, delimiter=';'))
        t = EtudiantUniversite(compt
            ,trow[0][0]
,trow[0][1]
,trow[0][2]
,trow[0][3]
,trow[0][4]
,trow[0][5]
,trow[0][6]
,trow[0][7]
,trow[0][8]
,trow[0][9]
,trow[0][10]
,trow[0][11]
,trow[0][12]
,trow[0][13]
,trow[0][14]
,trow[0][15]
,trow[0][16]
,trow[0][17]
,trow[0][18]
,trow[0][19]
,trow[0][20]
,trow[0][21]
,trow[0][22]
,trow[0][23]
,trow[0][24]
,trow[0][25]
,trow[0][26]
,trow[0][27]
,trow[0][28]
,trow[0][29]
,trow[0][30]
,trow[0][31]
,trow[0][32]
,trow[0][33]
,trow[0][34]
,trow[0][35]
,trow[0][36]
,trow[0][37]
,trow[0][38]
,trow[0][39]
,trow[0][40]
,trow[0][41]
,trow[0][42]
,trow[0][43]
,trow[0][44]
,trow[0][45]
,trow[0][46]
,trow[0][47]
,trow[0][48]
,trow[0][49]
,trow[0][50]
,trow[0][51]
,trow[0][52]
,trow[0][53]
,trow[0][54]
,trow[0][55]
,trow[0][56]
,trow[0][57]
,trow[0][58]
,trow[0][59]
,trow[0][60]
,trow[0][61]
,trow[0][62]
,trow[0][63]
,trow[0][64]
,trow[0][65]
,trow[0][66]
,trow[0][67]
,trow[0][68]
,trow[0][69]
,trow[0][70]
,trow[0][71]
,trow[0][72]
,trow[0][73]
,trow[0][74]
,trow[0][75]
,trow[0][76]
,trow[0][77])
        try:
            t.save()
            print("sauvegardé")
        except Exception as e:
            print(e)
            print(trow)
            break
        compt+=1


print("fin de l'importation de la table des effectifs etudiants")
