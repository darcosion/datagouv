from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^ecole/(?P<ecoleid>\d+)$', views.renduEcoleDocto, name='idecole'),
    url(r'^$', views.home, name='home'),
    url(r'description/$', views.description, name='description'),
    url(r'recherche/$', views.recherche, name='recherche'),
]

