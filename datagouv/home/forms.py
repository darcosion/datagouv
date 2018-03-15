from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom : ")
    envoyeur = forms.EmailField(label="Votre adresse mail")
    message = forms.CharField(widget=forms.Textarea)
    

class rechercheForm(forms.Form):
    #ici, on essaiera d'insérer les styles du form
    None

class LibelleForm(rechercheForm):
    libelle = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
