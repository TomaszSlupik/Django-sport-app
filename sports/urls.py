from django.urls import path
from sports.views import nowy_sportowiec, wyswietlenie, edytuj_sportowiec, usun_sportowiec


urlpatterns = [
    path('nowy/', nowy_sportowiec, name="nowy_sportowiec"),
    path('wszystkie/', wyswietlenie, name="wyswietlenie"),
    path('edytuj/<int:id>/', edytuj_sportowiec, name="edytuj_sportowiec"),
    path ('usun/<int:id>/', usun_sportowiec, name="usun_sportowiec"),
]