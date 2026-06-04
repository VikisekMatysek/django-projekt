from django.contrib import admin
from .models import Kategorie, Trener, Lekce, Rezervace, Zakaznik

admin.site.register(Kategorie)
admin.site.register(Trener)
admin.site.register(Lekce)
admin.site.register(Rezervace)
admin.site.register(Zakaznik)
