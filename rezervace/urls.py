from django.urls import path
from . import views

urlpatterns = [
    path('', views.uvod, name='domov'), 
    path('rozvrh/', views.seznam_lekci, name='rozvrh'),
    path('registrace/', views.registrace, name='registrace'),
    path('profil/', views.profil, name='profil'),
    path('kontakt/', views.kontakt, name='kontakt'),
]