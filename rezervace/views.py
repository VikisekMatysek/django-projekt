from django.shortcuts import render, redirect
from .models import Lekce, Rezervace, Zakaznik
from django.contrib.auth.forms import UserCreationForm


def uvod(request):
    """Zobrazí úvodní stránku"""
    return render(request, 'rezervace/index.html')

def seznam_lekci(request):
    """Zobrazí rozvrh"""
    try:
        lekce_list = list(Lekce.objects.all().order_by('datum_cas'))
    except Exception:
        lekce_list = []
    return render(request, 'rezervace/seznam_lekci.html', {'lekce_list': lekce_list})

def profil(request):
    """Zobrazí profil přihlášeného uživatele a jeho rezervace"""
    moje_rezervace = []
    if request.user.is_authenticated:
        try:
            zakaznik_obj = Zakaznik.objects.filter(jmeno=request.user.username).first()
            if zakaznik_obj:
                moje_rezervace = Rezervace.objects.filter(zakaznik=zakaznik_obj)
        except Exception:
            moje_rezervace = []
    return render(request, 'rezervace/profil.html', {'moje_rezervace': moje_rezervace})

def kontakt(request):
    return render(request, 'rezervace/kontakt.html')


def registrace(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrace.html', {'form': form})

