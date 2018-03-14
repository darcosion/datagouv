from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^ecole/(?P<ecoleid>\d+)$', views.renduEcoleDocto, name='idecole'),
    url(r'^$', views.home, name='home'),
    url(r'description/$', views.description, name='description'),
    url(r'recherche/$', views.recherche, name='recherche'),
    url(r'recherche/ecole/$', views.recherche_ecole, name='recherche_ecole'),
    url(r'recherche/promo/$', views.recherche_promo, name='recherche_promo'),
    url(r'recherche/fregion/$', views.recherche_effectifregional, name='recherche_effectifregional'),
    url(r'^fregion/(?P<regionid>\d+)$', views.rendufregion, name='idregion'),
    url(r'^promo/(?P<promoid>\d+)$',views.rendupromo, name='idpromo'),
    url(r'contact/$', views.contact, name='contact'),
]

