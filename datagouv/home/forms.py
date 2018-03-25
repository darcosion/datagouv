from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    captcha = CaptchaField()


class rechercheForm(forms.Form):
    #ici, on essaiera d'insérer les styles du form
    None

#Base : Ecole Doctorale :
class LibelleForm(rechercheForm):
    libelle = forms.CharField(label="Libelle ",max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

#Base : Étudiant Université :
class home_etudiantuniversiteForm(forms.Form):
    niveau = forms.CharField(label="Niveau", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Diplome = forms.CharField(label="Diplome", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Discipline = forms.CharField(label="Discipline", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Cycle_universitaire= forms.CharField(label="Cycle universitaire", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    rentreeAnnee = forms.IntegerField(label="Année de rentrée", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    DepartementUniteInscription = forms.CharField(label="Département de l'inscrit", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    AcademieUniteInscription = forms.CharField(label="Unité de l'académie de l'inscrit", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    NBEtudiantInscriptionAncienne= forms.IntegerField(label="Nombre d'ancien étudiant inscrit", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    NBTotalEtudiant= forms.IntegerField(label="Nombre total d'étudiant inscrit", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    NBEtudiantInscriptionPrincipale= forms.IntegerField(label="nombre d'étudiant à l'inscription principale", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    NBNouveauBacheliers= forms.IntegerField(label="nombre de nouveaux bacheliers", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))

#Base : Effectif Régional:
class EffectifregionalFrom(forms.Form):
    rentree_universitaire = forms.CharField(initial="rentree universitaire")
    secteur_de_l_etablissement = forms.CharField(initial="secteur de l'etablissement")
    effectif = forms.DecimalField(initial="discipline", required=False)
    geo_nom= forms.CharField(initial="geo nom", required=False)

#Base : BeneficiairesPrime :
class home_benefprimeexcellenceForm(forms.Form):
    etbissement = forms.CharField(label="",initial="etablissement")
    beneficiaires = forms.IntegerField(label="",initial="  beneficiaire")
    academie = forms.CharField(label="",initial="academie")
    annee= forms.IntegerField(label="",initial="annee")


#Forms inutille
"""
class auth_userForm(forms.Form):
    username = forms.CharField(label="", initial="login")
    first_name = forms.CharField(label="",initial="nom")
    last_name = forms.CharField(label="",initial="prénom")
    email= forms.CharField(label="",initial="mail")

class auth_permissionForm(forms.Form):
    name = forms.CharField(label="",initial="nom")
    codename = forms.CharField(label="",initial="son code")

class auth_groupeForm(forms.Form):
    name = forms.CharField(label="",initial="nom du groupe")
"""





