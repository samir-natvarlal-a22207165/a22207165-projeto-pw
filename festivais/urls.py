from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('listaFestivais/', views.festivais_view, name="listaFestivais"),
    path('festival/<int:festival_id>/', views.festival_view, name="festival"),
]