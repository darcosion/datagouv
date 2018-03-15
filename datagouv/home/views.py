from django.shortcuts import render

from .models import EcoleDoctorante, EtudiantUniversite, EffectifRegional, BenefPrimeExcellence
from .forms import ContactForm, LibelleForm



def home(request):

    return render(request, "base.html", locals())

def description(request):
    return render(request, "description.html", locals())

def recherche(request):
    return rendumenu(request, "recherche.html", locals())

def recherche_ecole(request):
    list_ecoledocto = EcoleDoctorante.objects.all()[:25]
    return rendumenu(request, "recherche.html", locals())

def recherche_ecolefiltre(request):
    if(request.path == "/recherche/ecole/libelle/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('libelle')[:25]
    if(request.path == "/recherche/ecole/univ/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('liste_tous_etablissements')[:25]
    path = request.path #debug
    return rendumenu(request, "recherche.html", locals())

def recherche_promo(request):
    list_promo = EtudiantUniversite.objects.all()[:25]
    return rendumenu(request, "recherche.html", locals())

def recherche_effectifregional(request):
    list_fregion = EffectifRegional.objects.all()[:25]
    return rendumenu(request, "recherche.html", locals())

def recherche_prime(request):
    list_prime = BenefPrimeExcellence.objects.all()[:25]
    return rendumenu(request, "recherche.html", locals())

def contact(request):
    contactform = ContactForm()
    return render(request, "contact.html", locals())

def renduEcoleDocto(request, ecoleid=0):
    ret = EcoleDoctorante.objects.get(numero=ecoleid)
    return render(request, "IdEcoleDoctorante.html", locals())

def rendufregion(request, regionid=0):
    ret = EffectifRegional.objects.get(id=regionid)
    return render(request, "effectifregional.html", locals()) 

def rendupromo(request, promoid=0):
    ret = EtudiantUniversite.objects.get(id=promoid)
    return render(request, "idPromo.html", locals())

def renduprime(request, primeid=0):
    ret = BenefPrimeExcellence.objects.get(id=primeid)
    return render(request, "idPrime.html", locals())



# décorateur d'ajout de form dans le menu
def rendumenu(request, uri, localvar):
    locals().update(localvar)
    libelle = LibelleForm()
    return render(request, uri, locals())
