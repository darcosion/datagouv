from django.db import models

#modèle d'école doctorante

class EcoleDoctorante(models.Model):
    numero = models.IntegerField(primary_key=True)
    signe = models.CharField(max_length=10)
    libelle = models.CharField(max_length=200)
    groupe_disciplinaire = models.CharField(max_length=200)
    toutes_les_disciplines = models.CharField(max_length=300)
    discipline_principale = models.CharField(max_length=200)
    localisation = models.CharField(max_length=400)
    liste_tous_etablissements = models.CharField(max_length=500)
    laboratoires_rattaches = models.CharField(max_length=400)
    annee_de_creation = models.PositiveIntegerField(null=True)
    annee_accreditation = models.PositiveIntegerField(null=True)
    duree_accreditation = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    code_etablissement_support = models.CharField(max_length=10, null=True)
    etablissement_support = models.CharField(max_length=100, null=True)
    code_etablissements_coaccredites = models.CharField(max_length=100, null=True)
    etablissements_coaccredites = models.CharField(max_length=500, null=True)
    codes_etablissements_associes = models.CharField(max_length=100, null=True)
    etablissements_associes = models.CharField(max_length=300, null=True)
    liste_codes_tous_etablissements = models.CharField(max_length=300, null=True)
    disciplines_secondaires  = models.CharField(max_length=400, null=True)
    identifiants_des_laboratoires = models.CharField(max_length=500, null=True)
    civilite_du_directeur = models.CharField(max_length=50, null=True)
    prenom_du_directeur = models.CharField(max_length=25, null=True)
    nom_du_directeur = models. CharField(max_length=100, null=True)
    telephone = models.PositiveIntegerField(null=True)
    mail = models.EmailField(null=True)
    site_web = models.URLField(max_length=500, null=True)
    adresse_postale = models.CharField(max_length=400, null=True)
    code_postal = models.PositiveIntegerField(null=True)
    code_commune = models.CharField(max_length=10, null=True)
    libelle_commune = models.CharField(max_length=100, null=True)
    code_unite_urbaine = models.CharField(max_length=50, null=True)
    libelle_unite_urbaine = models.CharField(max_length=50, null=True)
    code_departement = models.CharField(max_length=15, null=True)
    libelle_departement = models.CharField(max_length=50, null=True)
    code_academie = models.CharField(max_length=10, null=True)
    libelle_academie = models.CharField(max_length=100, null=True)
    code_region = models.CharField(max_length=10, null=True)
    libelle_region = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=30, null=True)
    coordonnees_geographiques = models.CharField(max_length=40, null=True)
    url_structures_de_recherche_actives = models.URLField(max_length=600, null=True)
    code_region_avant2016 = models.CharField(max_length=15, null=True)
    libelle_region_avant2016 = models.CharField(max_length=100, null=True)

#annee;diplome;numero_de_l_etablissement;etablissement;code_de_l_academie;academie;code_du_domaine;domaine;code_de_la_discipline;discipline;situation;remarque;nombre_de_reponses;taux_de_reponse;poids_de_la_discipline;taux_dinsertion;emplois_cadre_ou_professions_intermediaires;emplois_stables;emplois_a_temps_plein;salaire_net_median_des_emplois_a_temps_plein;salaire_brut_annuel_estime;de_diplomes_boursiers;taux_de_chomage_regional;salaire_net_mensuel_median_regional;emplois_cadre;emplois_exterieurs_a_la_region_de_luniversite;femmes;salaire_net_mensuel_regional_1er_quartile;salaire_net_mensuel_regional_3eme_quartile;cle_etab;cle_disc

#modèle d"effctif regional

class EffectifRegional(models.Model):
    rentree=models.PositiveIntegerField(null=True)
    rentree_universitaire=models.CharField(max_length=100,null=True) #Il y a du un - dans les données je ne peux pas le mettre en Integer
    niveau_geographique=models.CharField(max_length=100,null=True)
    geo_nom=models.CharField(max_length=100, null=True)
    regroupement=models.CharField(max_length=100, null=True)
    rgp_formations_ou_etablissements=models.CharField(max_length=200, null=True)
    secteur=models.CharField(max_length=20, null=True)
    secteur_de_l_etablissement=models.CharField(max_length=100, null=True)
    sexe=models.PositiveIntegerField(null=True)
    sexe_de_l_etudiant=models.CharField(max_length=20, null=True)
    effectif=models.FloatField(null=True)
    a_des_effectifs_dut=models.CharField(max_length=20, null=True)
    effectif_dut=models.CharField(max_length=20, null=True) #vide à revoir
    a_des_effectifs_ing=models.CharField(max_length=20, null=True)
    effectif_ing=models.CharField(max_length=20, null=True) #vide à revoir
    diffusable=models.CharField(max_length=20,null=True)
    donnees_diffusables=models.CharField(max_length=20,null=True)
    secret=models.CharField(max_length=20,null=True)
    donnees_soumises_au_secret_stat=models.CharField(max_length=20,null=True)
    niveau_geo=models.CharField(max_length=30,null=True)
    geo_id=models.CharField(max_length=10,null=True)
    reg_id=models.CharField(max_length=40,null=True)
    aca_id=models.CharField(max_length=20,null=True)
    dep_id=models.CharField(max_length=20,null=True)
    uucr_i=models.CharField(max_length=20,null=True)


# Create your models here.
