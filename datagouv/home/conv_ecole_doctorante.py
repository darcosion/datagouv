import csv

from .models import EcoleDoctorante

# attention, le délimiteur est sensé être un ";" mais
# s'il y a des doubles quotes, il ne doit pas être pris en compte
# dedans...

with open('fr-esr-ecoles_doctorales_annuaire.csv') as csvfile:
    # le delimiter permet de définir les entrée
    # le quotechar sépare les colonnes
    reader = csv.reader(csvfile, delimiter='\n')
    for row in list(reader)[1:]:
        trow = list(csv.reader(row, delimiter=';'))
        if(trow[0][24] == ''):
            trow[0][24] = None
        else:
            trow[0][24] = trow[0][24].replace(" ", "")[:10]
        t = EcoleDoctorante(trow[0][0]
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
,trow[0][43])
        t.save()


