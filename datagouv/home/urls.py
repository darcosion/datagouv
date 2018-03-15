from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    
    #Pages principales
    url(r'^$', views.home, name='home'),
    url(r'description/$', views.description, name='description'),
    url(r'recherche/$', views.recherche, name='recherche'),

    #Menu Ecole_Doctorante:
    url(r'recherche/ecole/$', views.recherche_ecole, name='recherche_ecole'),
    url(r'recherche/ecole/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_ecole, name='recherche_ecole'),

    #Menu Effectif_Étudiant:
    url(r'recherche/promo/$', views.recherche_promo, name='recherche_promo'),
    url(r'recherche/promo/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_promo, name='recherche_promo'),

    #Menu Effectif_Régionale:
    url(r'recherche/fregion/$', views.recherche_effectifregional, name='recherche_effectifregional'),
    url(r'recherche/fregion/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_effectifregional, name='recherche_effectifregional'),

    #Menu Prime & Bénéfiaires:
    url(r'recherche/prime/$', views.recherche_prime, name='recherche_prime'),
    url(r'recherche/prime/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_prime, name='recherche_prime'),
    
    #Page de recherche spécéfique :
    url(r'^fregion/(?P<regionid>\d+)$', views.rendufregion, name='idregion'),
    url(r'^promo/(?P<promoid>\d+)$',views.rendupromo, name='idpromo'),
    url(r'^prime/(?P<primeid>\d+)$',views.renduprime, name='idprime'),
    url(r'^ecole/(?P<ecoleid>\d+)$', views.renduEcoleDocto, name='idecole'),
    
    #Ecole Sous menu 
    url(r'^recherche/ecole/libelle/$', views.recherche_ecolefiltre, name='recherche_ecolelibelle'),
    url(r'^recherche/ecole/libelle/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_ecolefiltre, name='recherche_ecolelibelle'),
    url(r'^recherche/ecole/univ/$', views.recherche_ecolefiltre, name='recherche_ecoleuniv'),
    url(r'^recherche/ecole/univ/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_ecolefiltre, name='recherche_ecoleuniv'),
    
    #Promo Sous menu :
    url(r'^recherche/promo/etablissement/$', views.recherche_etudiantuniversite, name='recherche_etudiantuniversite'),
    url(r'^recherche/promo/etablissement/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_etudiantuniversite, name='recherche_etudiantuniversite'),
    url(r'^recherche/promo/commune/$', views.recherche_etudiantuniversite, name='recherche_etudiantuniversite'),
    url(r'^recherche/promo/commune/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_etudiantuniversite, name='recherche_etudiantuniversite'),

    #Fregion Sous menu :
    url(r'^recherche/fregion/formation/$', views.recherche_effectif, name='recherche_effectif'),
    url(r'^recherche/fregion/formation/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_effectif, name='recherche_effectif'),
    url(r'^recherche/fregion/commune/$', views.recherche_effectif, name='recherche_effectif'),
    url(r'^recherche/fregion/commune/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_effectif, name='recherche_effectif'),
    
    #Prime Sous menu :
    url(r'^recherche/prime/etablissement/$', views.recherche_primeben, name='recherche_primeben'),
    url(r'^recherche/prime/etablissement/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_primeben, name='recherche_primeben'),
    url(r'^recherche/prime/region/$', views.recherche_primeben, name='recherche_primeben'),
    url(r'^recherche/prime/region/(?P<idparcourd>\d+)/(?P<idparcourf>\d+)/$', views.recherche_primeben, name='recherche_primeben'),
   
    #Formulaire
    url(r'contact/$', views.contact, name='contact'),
]

