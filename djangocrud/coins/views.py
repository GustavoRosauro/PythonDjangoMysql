from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .forms import MoedaForm
from .models import Moeda


def index(request):
    moedas = Moeda.objects.all()
    return render(request, "coins/index.html",
                  {'moedas': moedas})


def inserir(request):
    print(str(request))
    if request.method == "POST":
        form = MoedaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/coins")
            except:
                pass
        else:
            moedas = Moeda.objects.all()
            return render(request, "coins/index.html",
                          {'moedas': moedas})


def deletar(request, id):
    moeda = Moeda.objects.get(id=id)
    moeda.delete()
    return redirect("/coins")


def edit(request, id):
    moeda = Moeda.objects.get(id=id)
    return render(request, "coins/index.html",
                  {'moeda': moeda})


def update(request, id):
    moeda = Moeda.objects.get(id=id)
    form = MoedaForm(request.POST, instance=moeda)
    if form.is_valid():
        form.save()
        return redirect("/coins")
    return redirect("/coins")
