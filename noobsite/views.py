from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view2(request):
    return HttpResponse("Primeiro Teste")

def index_view3(request):
    return HttpResponse("Um site Básico")

def index_view4(request):
    return HttpResponse("No response")