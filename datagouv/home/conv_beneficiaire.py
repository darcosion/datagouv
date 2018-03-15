import csv, os

from .models import BenefPrimeExcellence

# attention, le délimiteur est sensé être un ";" mais
# s'il y a des doubles quotes, il ne doit pas être pris en compte
# dedans...

compt = 1

with open('../fr-esr-pes-pedr-beneficiaires.csv') as csvfile:
    # le delimiter permet de définir les entrée
    # le quotechar sépare les colonnes
    reader = csv.reader(csvfile, delimiter='\n')
    for row in list(reader)[1:]:
        #print(compt)
        trow = list(csv.reader(row, delimiter=';'))
        trow[0][8]=trow[0][8].replace('\x92',"'")
        if(trow[0][15] == ''):
            trow[0][15] = None
        if(trow[0][5] == ''):
            trow[0][5] = None
        t = BenefPrimeExcellence(compt
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
)
        try:
            t.save()
        except Exception as e:
            print(t)
            print(e)
            break
        compt+=1


print("fin de l'importation de la table prime")
