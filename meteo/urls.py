from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('city/<int:id>/', views.city_view, name="city"),
    path('city/<int:id>/dia/<int:dia>/', views.city_dia_view, name="city_dia"),
]