from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sportowiec
from .forms import SportowiecForm
from django.contrib.auth.decorators import login_required


def wyswietlenie (request):
    calosc = Sportowiec.objects.all()
    return render(request, 'sport.html', {"sportowiec": calosc})

@login_required
def nowy_sportowiec (request):
    form = SportowiecForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wyswietlenie)

    return render(request, 'nowy_sportowiec.html', {"form": form})
@login_required
def edytuj_sportowiec (request, id):
    sport = get_object_or_404(Sportowiec, pk=id)
    form = SportowiecForm (request.POST or None, request.FILES or None, instance=sport)

    if form.is_valid():
        form.save()
        return redirect(wyswietlenie)

    return render(request, 'nowy_sportowiec.html',  {"form": form})
@login_required
def usun_sportowiec (request, id):
    form = get_object_or_404(Sportowiec, pk=id)

    if request.method == "POST":
        form.delete()
        return redirect(wyswietlenie)

    return render(request, "potwierdz.html", {"sport": form})