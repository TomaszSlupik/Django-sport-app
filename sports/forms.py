from django.forms import ModelForm
from .models import Sportowiec

class SportowiecForm (ModelForm):

    class Meta:
        model = Sportowiec
        fields = ['imie', 'nazwisko', 'rok_urodzenia', 'opis', 'zdjęcie']