from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('bandas/', views.listaBandas_view, name="listaBandas"),
    path('albuns/', views.listaAlbuns_view, name="listaAlbuns"),
    path('musicas/', views.listaMusicas_view, name="listaMusicas"),
    path('banda/<int:banda_id>/', views.banda_view, name="banda"),
    path('album/<int:album_id>/', views.album_view, name="album"),
    path('musica/<int:musica_id>/', views.musica_view, name="musica"),
    path('banda/novo/',views.novo_banda_view,name="novo_banda"),
    path('album/novo/',views.novo_album_view,name="novo_album"),
    path('musica/novo/',views.novo_musica_view,name="novo_musica"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
    path('album/<int:album_id>/edita', views.edita_album_view,name="edita_album"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('album/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),
    path('registo/', views.registo_view, name="registo_bandas"),
    path('login/', views.login_view, name="login_bandas"),
    path('logout/', views.logout_view, name="logout_bandas"),
]