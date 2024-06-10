from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('artigo/<int:artigo_id>/', views.detalhes_artigo, name='detalhes_artigo'),
    path('artigo/novo/',views.novo_artigo_view,name="novo_artigo"),
    path('comentario/novo/',views.novo_comentario_view,name="novo_comentario"),
    path('autor/novo/',views.novo_autor_view,name="novo_autor"),
    path('avaliacao/novo/',views.novo_avaliacao_view,name="novo_avaliacao"),
    path('categoria/novo/',views.novo_categoria_view,name="novo_categoria"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
    path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    path('comentario/<int:comentario_id>/edita', views.edita_comentario_view,name="edita_comentario"),
    path('comentario/<int:comentario_id>/apaga', views.apaga_comentario_view,name="apaga_comentario"),
    path('categoria/<int:categoria_id>/edita', views.edita_categoria_view,name="edita_categoria"),
    path('categoria/<int:categoria_id>/apaga', views.apaga_categoria_view,name="apaga_categoria"),
    path('avaliacao/<int:avaliacao_id>/edita', views.edita_avaliacao_view,name="edita_avaliacao"),
    path('avaliacao/<int:avaliacao_id>/apaga', views.apaga_avaliacao_view,name="apaga_avaliacao"),
]
