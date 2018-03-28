from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    captcha = CaptchaField()


class rechercheForm(forms.Form):
    #ici, on essaiera d'insérer les styles du form
    None

#Base : Étudiant Université :
class home_etudiantuniversiteForm(forms.Form):
    niveau = forms.CharField(label="Niveau", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Diplome = forms.CharField(label="Diplome", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Discipline = forms.CharField(label="Discipline", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Cycle_universitaire= forms.CharField(label="Cycle universitaire", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    rentreeAnnee = forms.IntegerField(label="Année de rentrée", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    DepartementUniteInscription = forms.CharField(label="Département de l'inscrit", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    AcademieUniteInscription = forms.CharField(label="Unité de l'académie de l'inscrit", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    NBTotalEtudiant= forms.IntegerField(label="Nombre total d'étudiant inscrit", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    NBEtudiantInscriptionPrincipale= forms.IntegerField(label="Nombre d'étudiant à l'inscription principale", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    NBNouveauBacheliers= forms.IntegerField(label="Nombre de nouveaux bacheliers", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))

#Base : Effectif Régional:
class EffectifregionalFrom(forms.Form):
    rentree_universitaire = forms.CharField(label="Rentrée Universitaire  ",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    secteur_de_l_etablissement = forms.CharField(label="Secteur de l'établissement ",required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    effectif = forms.DecimalField(label="Effectif", required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    geo_nom= forms.CharField(label="Commune ", required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))

#Base : BeneficiairesPrime :
class home_benefprimeexcellenceForm(forms.Form):
    etbissement = forms.CharField(label="Établissement ",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    beneficiaires = forms.IntegerField(label="Béneficiaire :",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    academie = forms.CharField(label="Académie :",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    annee= forms.IntegerField(label="Année :",required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))

#Base:ecloedoctorante
class home_ecoledoctorante(forms.Form):
    libelle = forms.CharField(label="Libellé",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    ville = forms.CharField(label="Ville",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    libelle_region_avant2016 = forms.IntegerField(label="Libellé de la région",required=False, widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    nom_du_directeur = forms.CharField(label="Nom du directeur",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    mail= forms.EmailField(label="Mail du directeur",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    site_web = forms.CharField(label="Site web de l'établissement ",required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))





