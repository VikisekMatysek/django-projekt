from django.db import models
from django.contrib.auth.models import User

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"
    class Meta:
        db_table = 'rezervace_zakaznik'

class Kategorie(models.Model):
    nazev = models.CharField(max_length=50)
    def __str__(self):
        return self.nazev
    class Meta:
        db_table = 'rezervace_kategorie'

class Trener(models.Model):
    jmeno = models.CharField(max_length=100)
    specializace = models.CharField(max_length=100)
    def __str__(self):
        return self.jmeno
    class Meta:
        db_table = 'rezervace_trener'

class Lekce(models.Model):
    nazev = models.CharField(max_length=100)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    trener = models.ForeignKey(Trener, on_delete=models.CASCADE)
    datum_cas = models.DateTimeField()
    kapacita = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.nazev} ({self.datum_cas})"
    class Meta:
        db_table = 'rezervace_lekce'

class Rezervace(models.Model):
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE)
    lekce = models.ForeignKey(Lekce, on_delete=models.CASCADE)
    vytvoreno = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'rezervace_rezervace'

