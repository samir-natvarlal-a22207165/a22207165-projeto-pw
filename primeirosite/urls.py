from django.urls import path
from . import views

app_name = 'primeirosite'

urlpatterns = [
    path('caracteristicas/', views.caracteristicas_view, name='caracteristicas'),
    path('descricao/', views.descricao_view, name='descricao'),
    path('diacronia/', views.diacronia_view, name='diacronia'),
]