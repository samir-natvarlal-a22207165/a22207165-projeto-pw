from django.urls import path
from . import views

app_name = 'portefolio'

urlpatterns = [
    path('cursos/', views.cursos_view, name="cursos"),
    path('curso/<int:curso_id>/', views.curso_view, name="curso"),
    path('disciplinas/', views.disciplinas_view, name="disciplinas"),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name="disciplina"),
    path('projetos/', views.projetos_view, name="projetos"),
    path('projeto/<int:projeto_id>/', views.projeto_view, name="projeto"),

    path('curso/novo/',views.novo_curso_view,name="novo_curso"),
    path('curso/<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),
    path('curso/<int:curso_id>/apaga', views.apaga_curso_view,name="apaga_curso"),

    path('areaCientifica/novo/',views.novo_areaCientifica_view,name="novo_areaCientifica"),
    path('areaCientifica/<int:areaCientifica_id>/edita', views.edita_areaCientifica_view,name="edita_areaCientifica"),
    path('areaCientifica/<int:areaCientifica_id>/apaga', views.apaga_areaCientifica_view,name="apaga_areaCientifica"),

    path('disciplina/novo/',views.novo_disciplina_view,name="novo_disciplina"),
    path('disciplina/<int:disciplina_id>/edita', views.edita_disciplina_view,name="edita_disciplina"),
    path('disciplina/<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),

    path('projeto/novo/',views.novo_projeto_view,name="novo_projeto"),
    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),

    path('linguagemProgramacao/novo/',views.novo_linguagemProgramacao_view,name="novo_linguagemProgramacao"),
    path('linguagemProgramacao/<int:linguagemProgramacao_id>/edita', views.edita_linguagemProgramacao_view,name="edita_linguagemProgramacao"),
    path('linguagemProgramacao/<int:linguagemProgramacao_id>/apaga', views.apaga_linguagemProgramacao_view,name="apaga_linguagemProgramacao"),

    path('docente/novo/',views.novo_docente_view,name="novo_docente"),
    path('docente/<int:docente_id>/edita', views.edita_docente_view,name="edita_docente"),
    path('docente/<int:docente_id>/apaga', views.apaga_docente_view,name="apaga_docente"),
]