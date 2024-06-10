from django.shortcuts import render

def caracteristicas_view(request):
    return render(request, "primeirosite/caracteristicas.html")

def descricao_view(request):
    return render(request, "primeirosite/descricao.html")

def diacronia_view(request):
    return render(request, "primeirosite/diacronia.html")