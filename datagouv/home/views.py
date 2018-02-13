from django.shortcuts import render

from .models import EcoleDoctorante

# Create your views here.

def home(request):

    return render(request, "base.html", locals())

def renduEcoleDocto(request, ecoleid=0):
    ret = EcoleDoctorante.objects.get(numero=ecoleid)
    return render(request, "IdEcoleDoctorante.html", locals())
