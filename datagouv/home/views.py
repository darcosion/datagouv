from django.shortcuts import render

from .models import EcoleDoctorante
from .forms import ContactForm

# Create your views here.

def home(request):

    return render(request, "base.html", locals())

def description(request):

    return render(request, "description.html", locals())

def recherche(request):
    list_ecoledocto = EcoleDoctorante.objects.all()[:25]
    return render(request, "recherche.html", locals())

def contact(request):
    contactform = ContactForm()
    return render(request, "contact.html", locals())

def renduEcoleDocto(request, ecoleid=0):
    ret = EcoleDoctorante.objects.get(numero=ecoleid)
    return render(request, "IdEcoleDoctorante.html", locals())
