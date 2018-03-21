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


class home_etudiantuniversiteForm(forms.Form):
    niveau = forms.CharField(label="",initial="niveau")
    Diplome = forms.CharField(label="",initial="diplome")
    Discipline = forms.CharField(label="",initial="discipline")
    Cycle_universitaire= forms.CharField(label="",initial="Cycle universitaire")
    rentreeAnnee = forms.IntegerField(label="",initial="annee de la rentrée", required=False)
    DepartementUniteInscription = forms.CharField(label="",initial="Departement de l'inscription")
    AcademieUniteInscription = forms.CharField(label="",initial="Academie Unite Inscription")
    NBEtudiantInscriptionAncienne= forms.IntegerField(label="",initial="nombre d'ancienne étudiant inscrit ", required=False)
    NBTotalEtudiant= forms.IntegerField(label="",initial="nombre total étudiant inscrit ", required=False)
    NBEtudiantInscriptionPrincipale= forms.IntegerField(label="",initial="nombre d'étudiant à l'inscription principale", required=False)
    NBNouveauBacheliers= forms.IntegerField(label="",initial="nombre de nouveaux bacheleirs", required=False)


class EffectifregionalFrom(forms.Form):
    rentree_universitaire = forms.CharField(initial="rentree universitaire")
    secteur_de_l_etablissement = forms.CharField(initial="secteur de l'etablissement")
    effectif = forms.DecimalField(initial="discipline", required=False)
    geo_nom= forms.CharField(initial="geo nom", required=False)

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

class home_benefprimeexcellenceForm(forms.Form):
    etbissement = forms.CharField(label="",initial="etablissement")
    beneficiaires = forms.IntegerField(label="",initial="  beneficiaire")
    academie = forms.CharField(label="",initial="academie")
    annee= forms.IntegerField(label="",initial="annee")




