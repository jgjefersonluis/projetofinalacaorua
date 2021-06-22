from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from graficos.models import Beneficio, Substancias, Saude, Genero, FaixaEtaria, Etnia


def beneficio(request):
    return render(request, 'beneficio.html')

def etnia(request):
    return render(request, 'etnia.html')

def faixaetaria(request):
    return render(request, 'faixa-etaria.html')

def genero(request):
    return render(request, 'genero.html')

def saude(request):
    return render(request, 'saude.html')

def substancias(request):
    return render(request, 'substancias.html')


def pie_chart(request):
    labels = []
    data = []

    queryset = Beneficio.objects.order_by('-population')[:9]
    for beneficio in queryset:
        labels.append(beneficio.name)
        data.append(beneficio.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })

def pie_chart1(request):
    labels = []
    data = []

    queryset = Etnia.objects.order_by('-population')[:9]
    for etnia in queryset:
        labels.append(etnia.name)
        data.append(etnia.population)

    return render(request, 'pie_chart1.html', {
        'labels': labels,
        'data': data,
    })

def pie_chart2(request):
    labels = []
    data = []

    queryset = FaixaEtaria.objects.order_by('-population')[:9]
    for faixaetaria in queryset:
        labels.append(faixaetaria.name)
        data.append(faixaetaria.population)

    return render(request, 'pie_chart2.html', {
        'labels': labels,
        'data': data,
    })

def pie_chart3(request):
    labels = []
    data = []

    queryset = Genero.objects.order_by('-population')[:9]
    for renda in queryset:
        labels.append(genero.name)
        data.append(genero.population)

    return render(request, 'pie_chart3.html', {
        'labels': labels,
        'data': data,
    })

def pie_chart4(request):
    labels = []
    data = []

    queryset = Saude.objects.order_by('-population')[:9]
    for saude in queryset:
        labels.append(saude.name)
        data.append(saude.population)

    return render(request, 'pie_chart3.html', {
        'labels': labels,
        'data': data,
    })

def pie_chart5(request):
    labels = []
    data = []

    queryset = Substancias.objects.order_by('-population')[:9]
    for city in queryset:
        labels.append(substancias.name)
        data.append(substancias.population)

    return render(request, 'pie_chart5.html', {
        'labels': labels,
        'data': data,
    })