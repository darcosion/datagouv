from django.shortcuts import render

from .models import EcoleDoctorante, EtudiantUniversite, EffectifRegional, BenefPrimeExcellence, ContactCommentaire
from .forms import ContactForm, LibelleForm, home_etudiantuniversiteForm, EffectifregionalFrom, home_benefprimeexcellenceForm



def description(request):
    return render(request, "description.html", locals())

def recherche(request):
    libelleform = LibelleForm()
    home_etudiantuniversiteform = home_etudiantuniversiteForm()
    Effectifregionalfrom = EffectifregionalFrom()
    home_benefprimeexcellenceform = home_benefprimeexcellenceForm()
    return rendumenu(request, "recherche.html", locals())

def recherche_ecole(request, idparcourd=0, idparcourf=25):
    list_ecoledocto = EcoleDoctorante.objects.all()[int(idparcourd):int(idparcourf)]
    return rendumenu(request, "recherche.html", locals())

def recherche_post_ecolefiltre(request, idparcourd=0, idparcourf=25):
    if(request.method == 'POST'):
        libelleform = LibelleForm(request.POST)
        if(libelleform.is_valid()):
            list_ecoledocto = EcoleDoctorante.objects.filter(libelle__contains=libelleform.cleaned_data['libelle'])[int(idparcourd):int(idparcourf)]
        else:
            erreur = libelleform.errors
    return rendumenu(request, "recherche.html", locals())

def recherche_post_promo(request, idparcourd=0, idparcourf=25):
    if(request.method == 'POST'):
        home_etudiantuniversiteform = home_etudiantuniversiteForm(request.POST)
        if(home_etudiantuniversiteform.is_valid()):
            list_promo = False
            if(home_etudiantuniversiteform.cleaned_data['niveau'] != ""):
                list_promo = EtudiantUniversite.objects.filter(niveau__contains=home_etudiantuniversiteform.cleaned_data['niveau'])
            if(home_etudiantuniversiteform.cleaned_data['Diplome'] != ""):
                if(list_promo):
                    list_promo.filter(diplome__contains=home_etudiantuniversiteform.cleaned_data['Diplome'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(diplome__contains=home_etudiantuniversiteform.cleaned_data['Diplome'])
            if(home_etudiantuniversiteform.cleaned_data['Discipline'] != ""):
                if(list_promo):
                    list_promo.filter(Discipline__contains=home_etudiantuniversiteform.cleaned_data['Discipline'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(Discipline__contains=home_etudiantuniversiteform.cleaned_data['Discipline'])
            if(home_etudiantuniversiteform.cleaned_data['Cycle_universitaire'] != ""):
                if(list_promo):
                    list_promo.filter(Cycle_universitaire__contains=home_etudiantuniversiteform.cleaned_data['Cycle_universitaire'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(Cycle_universitaire__contains=home_etudiantuniversiteform.cleaned_data['Cycle_universitaire'])
            if(home_etudiantuniversiteform.cleaned_data['rentreeAnnee'] != None):
                if(list_promo):
                    list_promo.filter(rentreeAnnee__contains=home_etudiantuniversiteform.cleaned_data['rentreeAnnee'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(rentreeAnnee__contains=home_etudiantuniversiteform.cleaned_data['rentreeAnnee'])
            if(home_etudiantuniversiteform.cleaned_data['DepartementUniteInscription'] != ""):
                if(list_promo):
                    list_promo.filter(DepartementUniteInscription__contains=home_etudiantuniversiteform.cleaned_data['DepartementUniteInscription'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(DepartementUniteInscription__contains=home_etudiantuniversiteform.cleaned_data['DepartementUniteInscription'])
            if(home_etudiantuniversiteform.cleaned_data['AcademieUniteInscription'] != ""):
                if(list_promo):
                    list_promo.filter(AcademieUniteInscription__contains=home_etudiantuniversiteform.cleaned_data['AcademieUniteInscription'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(AcademieUniteInscription__contains=home_etudiantuniversiteform.cleaned_data['AcademieUniteInscription'])
            if(home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionAncienne'] != None):
                if(list_promo):
                    list_promo.filter(NBEtudiantInscriptionAncienne__contains=home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionAncienne'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(NBEtudiantInscriptionAncienne__contains=home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionAncienne'])
            if(home_etudiantuniversiteform.cleaned_data['NBTotalEtudiant'] != None):
                if(list_promo):
                    list_promo.filter(NBTotalEtudiant__contains=home_etudiantuniversiteform.cleaned_data['NBTotalEtudiant'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(NBTotalEtudiant__contains=home_etudiantuniversiteform.cleaned_data['NBTotalEtudiant'])
            if(home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionPrincipale'] != None):
                if(list_promo):
                    list_promo.filter(NBEtudiantInscriptionPrincipale__contains=home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionPrincipale'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(NBEtudiantInscriptionPrincipale__contains=home_etudiantuniversiteform.cleaned_data['NBEtudiantInscriptionPrincipale'])
            if(home_etudiantuniversiteform.cleaned_data['NBNouveauBacheliers'] != None):
                if(list_promo):
                    list_promo.filter(NBNouveauBacheliers__contains=home_etudiantuniversiteform.cleaned_data['NBNouveauBacheliers'])
                else:
                    list_promo = EtudiantUniversite.objects.filter(NBNouveauBacheliers__contains=home_etudiantuniversiteform.cleaned_data['NBNouveauBacheliers'])
            if(list_promo):
                list_promo = list_promo[int(idparcourd):int(idparcourf)]
        else:
            erreur = home_etudiantuniversiteForm.errors
    return rendumenu(request, "recherche.html", locals())

def recherche_post_effectifregion(request, idparcourd=0, idparcourf=25):
    if(request.method == 'POST'):
        Effectifregionalfrom = EffectifregionalFrom(request.POST)
        if(Effectifregionalfrom.is_valid()):
            list_fregion = False
            if(Effectifregionalfrom.cleaned_data['rentree_universitaire'] != ""):
                list_fregion = EffectifRegional.objects.filter(rentree_universitaire__contains=Effectifregionalfrom.cleaned_data['rentree_universitaire'])
            if(Effectifregionalfrom.cleaned_data['secteur_de_l_etablissement'] != ""):
                if(list_fregion):
                    list_fregion.filter(secteur_de_l_etablissement__contains=Effectifregionalfrom.cleaned_data['rentree_universitaire'])
                else:
                    list_fregion = EffectifRegional.objects.filter(secteur_de_l_etablissement__contains=Effectifregionalfrom.cleaned_data['rentree_universitaire'])
                if(list_fregion):
                    list_fregion.filter(effectif__contains=Effectifregionalfrom.cleaned_data['effectif'])
                else:
                    list_fregion = EffectifRegional.objects.filter(effectif__contains=Effectifregionalfrom.cleaned_data['effectif'])
            if(Effectifregionalfrom.cleaned_data['geo_nom'] != None):
                if(list_fregion):
                    list_fregion.filter(geo_nom__contains=Effectifregionalfrom.cleaned_data['geo_nom'])
                else:
                    list_fregion = EffectifRegional.objects.filter(geo_nom__contains=Effectifregionalfrom.cleaned_data['geo_nom'])
            if(list_fregion):
                list_fregion = list_fregion[int(idparcourd):int(idparcourf)]
        else:
            erreur = EffectifregionalFrom.errors
    return rendumenu(request, "recherche.html", locals())

def recherche_post_prime(request, idparcourd=0, idparcourf=25):
    if(request.method == 'POST'):
        home_benefprimeexcellenceform = home_benefprimeexcellenceForm(request.POST)
        if(home_benefprimeexcellenceform.is_valid()):
            list_prime = False
            if(home_benefprimeexcellenceform.cleaned_data['beneficiaires'] != None):
                list_prime = BenefPrimeExcellence.objects.filter(beneficiaires__contains=home_benefprimeexcellenceform.cleaned_data['beneficiaires'])
            if(home_benefprimeexcellenceform.cleaned_data['etbissement'] != ""):
                if(list_prime):
                    list_prime.filter(etbissement__contains=home_benefprimeexcellenceform.cleaned_data['etablissement'])
                else:
                    list_prime = BenefPrimeExcellence.objects.filter(etbissement__contains=home_benefprimeexcellenceform.cleaned_data['etablissement'])
            if(home_benefprimeexcellenceform.cleaned_data['academie'] != ""):
                if(list_prime):
                    list_prime.filter(academie__contains=home_benefprimeexcellenceform.cleaned_data['academie'])
                else:
                    list_prime = BenefPrimeExcellence.objects.filter(academie__contains=home_benefprimeexcellenceform.cleaned_data['academie'])
            if(home_benefprimeexcellenceform.cleaned_data['annee'] != None):
                if(list_prime):
                    list_prime.filter(annee__contains=home_benefprimeexcellenceform.cleaned_data['annee'])
                else:
                    list_prime = BenefPrimeExcellence.objects.filter(annee__contains=home_benefprimeexcellenceform.cleaned_data['annee'])
            if(list_prime):
                list_prime = list_prime[int(idparcourd):int(idparcourf)]
        else:
            erreur = home_benefprimeexcellenceForm.errors
    return rendumenu(request, "recherche.html", locals())

def recherche_post_utilisateur(request, idparcourd=0, idparcourf=25):
    if(request.method == 'POST'):
        auth_userform = auth_userForm(request.POST)
        if(auth_userform.is_valid()):
            list_fregion = EffectifRegional.objects.filter(rentree_universitaire__contains=auth_userform.cleaned_data['rentree_universitaire'])[int(idparcourd):int(idparcourf)]
        else:
            erreur = auth_userForm.errors
    return rendumenu(request, "recherche.html", locals())

def recherche_ecolefiltre(request, idparcourd=0, idparcourf=25):
    if(request.path == "/recherche/ecole/libelle/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('libelle')[int(idparcourd):int(idparcourf)]
    if(request.path == "/recherche/ecole/univ/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('liste_tous_etablissements')[int(idparcourd):int(idparcourf)]
    path = request.path #debug
    return rendumenu(request, "recherche.html", locals())

def recherche_primeben(request, idparcourd=0, idparcourf=25):
    if(request.path == "/recherche/prime/etablissement/"):
        list_prime = BenefPrimeExcellence.objects.order_by('etablissement')[int(idparcourd):int(idparcourf)]
    if(request.path == "/recherche/prime/region/"):
        list_prime = BenefPrimeExcellence.objects.order_by('region')[int(idparcourd):int(idparcourf)]
    path = request.path #debug
    return rendumenu(request, "recherche.html", locals())

def recherche_effectif(request, idparcourd=0, idparcourf=25):
    if(request.path == "/recherche/fregion/commune/"):
        list_fregion = EffectifRegional.objects.order_by('geo_nom')[int(idparcourd):int(idparcourf)]
    if(request.path == "/recherche/fregion/formation/"):
        list_fregion = EffectifRegional.objects.order_by('rgp_formations_ou_etablissements')[int(idparcourd):int(idparcourf)]
    path = request.path #debug
    return rendumenu(request, "recherche.html", locals())

def recherche_etudiantuniversite(request, idparcourd=0, idparcourf=25):
    if(request.path == "/recherche/promo/etablissement/"):
        list_promo = EtudiantUniversite.objects.order_by('etablissementId')[int(idparcourd):int(idparcourf)]
    if(request.path == "/recherche/promo/commune/"):
        list_promo = EtudiantUniversite.objects.order_by('SiegeEtablissement')[int(idparcourd):int(idparcourf)]
    path = request.path #debug
    return rendumenu(request, "recherche.html", locals())

def recherche_promo(request, idparcourd=0, idparcourf=25):
    list_promo = EtudiantUniversite.objects.all()[int(idparcourd):int(idparcourf)]
    return rendumenu(request, "recherche.html", locals())

def recherche_effectifregional(request, idparcourd=0, idparcourf=25):
    list_fregion = EffectifRegional.objects.all()[int(idparcourd):int(idparcourf)]
    return rendumenu(request, "recherche.html", locals())

def recherche_prime(request, idparcourd=0, idparcourf=25):
    list_prime = BenefPrimeExcellence.objects.all()[int(idparcourd):int(idparcourf)]
    return rendumenu(request, "recherche.html", locals())

def contact(request):
    list_com = ContactCommentaire.objects.all()
    if(request.method == 'POST'):
        contactform = ContactForm(request.POST)
        if(contactform.is_valid()):
            newcom = ContactCommentaire(nom=contactform.cleaned_data['nom'],
            commentaire=contactform.cleaned_data['message'])
            newcom.save()
        else:
            erreur = contactform.errors
    else:
        contactform = ContactForm()
    return render(request, "contact.html", locals())

def renduEcoleDocto(request, ecoleid=0):
    ret = EcoleDoctorante.objects.get(numero=ecoleid)
    return rendumenu(request, "IdEcoleDoctorante.html", locals())

def rendufregion(request, regionid=0):
    ret = EffectifRegional.objects.get(id=regionid)
    return rendumenu(request, "effectifregional.html", locals())

def rendupromo(request, promoid=0):
    ret = EtudiantUniversite.objects.get(id=promoid)
    return rendumenu(request, "idPromo.html", locals())

def renduprime(request, primeid=0):
    ret = BenefPrimeExcellence.objects.get(id=primeid)
    return rendumenu(request, "idPrime.html", locals())



# wrapper d'ajout de form dans le menu
def rendumenu(request, uri, localvar):
    if 'idparcourd' in localvar:
        if(int(localvar['idparcourd']) >= 25):
            precparcourd = int(localvar['idparcourd'])-25
            precparcourdf = int(localvar['idparcourf'])-25
            print("retour (" + localvar['idparcourd'] + ")" + "(" + str(precparcourd) + ")")
        localvar['idparcourd']=int(localvar['idparcourd'])+25
        localvar['idparcourf']=int(localvar['idparcourf'])+25

    locals().update(localvar)

    return render(request, uri, locals())
