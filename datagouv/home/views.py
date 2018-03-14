from django.shortcuts import render

from .models import EcoleDoctorante, EtudiantUniversite, EffectifRegional, BenefPrimeExcellence
from .forms import ContactForm

# Create your views here.

def home(request):

    return render(request, "base.html", locals())

def description(request):
    return render(request, "description.html", locals())

def recherche(request):
    return render(request, "recherche.html", locals())

def recherche_ecole(request):
    list_ecoledocto = EcoleDoctorante.objects.all()[:25]
    return render(request, "recherche.html", locals())

def recherche_promo(request):
    list_promo = EtudiantUniversite.objects.all()[:25]
    return render(request, "recherche.html", locals())

def recherche_effectifregional(request):
    list_fregion = EffectifRegional.objects.all()[:25]
    return render(request, "recherche.html", locals())

def recherche_prime(request):
    list_prime = BenefPrimeExcellence.objects.all()[:25]
    return render(request, "recherche.html", locals())

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