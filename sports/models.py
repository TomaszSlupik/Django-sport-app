from django.db import models

class Sportowiec (models.Model):

    imie = models.CharField (max_length=10, blank = False)
    nazwisko = models.CharField (max_length=20, blank = False)
    rok_urodzenia = models.DateField (null= True, blank= True)
    opis = models.TextField (default="")
    zdjęcie =models.ImageField (upload_to="zdjecia", null= True, blank=True)

    def imie_nazwisko(self):
        return "{} {}".format(self.imie, self.nazwisko)

    def __str__ (self):
        return self.imie_nazwisko()