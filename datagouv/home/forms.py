from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom : ")
    envoyeur = forms.EmailField(label="Votre adresse mail")
    message = forms.CharField(widget=forms.Textarea)
    
