from django.shortcuts import render
from festivais.models import Festival

def festivais_view(request):
    context = {
      'festivais': Festival.objects.all().order_by('nome'),
    }

    return render(request, "festivais/listaFestivais.html", context)

def festival_view(request, festival_id):
    context = {
      'festival': Festival.objects.get(id=festival_id),
    }

    return render(request, "festivais/festival.html", context)
