from django.shortcuts import render

from .models import EcoleDoctorante, EtudiantUniversite, EffectifRegional, BenefPrimeExcellence
from .forms import ContactForm, LibelleForm



def home(request):
    return render(request, "base.html", locals())

def description(request):
    return render(request, "description.html", locals())

def recherche(request):
    return rendumenu(request, "recherche.html", locals())

def recherche_ecole(request, idparcourd=0, idparcourf=25):
    list_ecoledocto = EcoleDoctorante.objects.all()[int(idparcourd):int(idparcourf)]
    return rendumenu(request, "recherche.html", locals())

def recherche_ecolefiltre(request, idparcourd=0, idparcourf=25):
    if(request.path == "/recherche/ecole/libelle/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('libelle')[int(idparcourd):int(idparcourf)]
    if(request.path == "/recherche/ecole/univ/"):
        list_ecoledocto = EcoleDoctorante.objects.order_by('liste_tous_etablissements')[int(idparcourd):int(idparcourf)]
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
    if 'idparcoud' in localvar:
        localvar['idparcourd']=int(localvar['idparcourd'])+25
        localvar['idparcourf']=int(localvar['idparcourf'])+25
    locals().update(localvar)
    libelle = LibelleForm()
    return render(request, uri, locals())
