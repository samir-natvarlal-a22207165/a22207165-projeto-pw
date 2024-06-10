from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('about/', views.about_view, name="about"),
    path('cv/', views.cv_view, name="cv"),
    path('other/', views.other_view, name="other"),
    path('tech/', views.tech_view, name="tech"),
]