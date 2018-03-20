from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    captcha = CaptchaField()


class rechercheForm(forms.Form):
    #ici, on essaiera d'insérer les styles du form
    None

class LibelleForm(rechercheForm):
    libelle = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
