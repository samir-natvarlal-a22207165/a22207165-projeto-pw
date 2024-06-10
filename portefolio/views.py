from django.shortcuts import render, redirect
from portefolio.models import Curso, Disciplina, Projeto, AreaCientifica, Docente, LinguagemProgramacao
from .forms import CursoForm, DisciplinaForm, ProjetoForm, AreaCientificaForm, DocenteForm, LinguagemProgramacaoForm
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, "portefolio/index.html")

def curso_view(request, curso_id):
    context = {
      'curso': Curso.objects.get(id=curso_id),
    }
    return render(request, "portefolio/curso.html", context)

def cursos_view(request):
    context = {
      'cursos': Curso.objects.all().order_by('nome'),
    }
    return render(request, "portefolio/cursos.html", context)

def disciplinas_view(request):
    context = {
      'disciplinas': Disciplina.objects.all().order_by('nome'),
    }
    return render(request, "portefolio/disciplinas.html", context)

def disciplina_view(request, disciplina_id):
    context = {
      'disciplina': Disciplina.objects.get(id=disciplina_id),
    }
    return render(request, "portefolio/disciplina.html", context)

def projetos_view(request):
    context = {
      'projetos': Projeto.objects.all().order_by('nome_projeto'),
    }
    return render(request, "portefolio/projetos.html", context)

def projeto_view(request, projeto_id):
    context = {
      'projeto': Projeto.objects.get(id=projeto_id),
    }
    return render(request, "portefolio/projeto.html", context)

@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:cursos')
    context = {'form': form}
    return render(request, 'portefolio/novo_curso.html', context)

@login_required
def novo_areaCientifica_view(request):
    form = AreaCientificaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:disciplinas')
    context = {'form': form}
    return render(request, 'portefolio/novo_areaCientifica.html', context)

@login_required
def novo_disciplina_view(request):
    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:disciplinas')
    context = {'form': form}
    return render(request, 'portefolio/novo_disciplina.html', context)

@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:projetos')
    context = {'form': form}
    return render(request, 'portefolio/novo_projeto.html', context)

@login_required
def novo_linguagemProgramacao_view(request):
    form = LinguagemProgramacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:disciplinas')
    context = {'form': form}
    return render(request, 'portefolio/novo_linguagemProgramacao.html', context)

@login_required
def novo_docente_view(request):
    form = DocenteForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portefolio:disciplinas')
    context = {'form': form}
    return render(request, 'portefolio/novo_docente.html', context)



@login_required
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('portefolio:cursos')
    else:
        form = CursoForm(instance=curso)
    context = {'form': form, 'curso':curso}
    return render(request, 'portefolio/edita_curso.html', context)

@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('portefolio:disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'portefolio/edita_disciplina.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portefolio:projetos')
    else:
        form = ProjetoForm(instance=projeto)
    context = {'form': form, 'projeto': projeto}
    return render(request, 'portefolio/edita_projeto.html', context)

@login_required
def edita_areaCientifica_view(request, areaCientifica_id):
    areaCientifica = AreaCientifica.objects.get(id=areaCientifica_id)
    if request.POST:
        form = AreaCientificaForm(request.POST or None, instance=areaCientifica)
        if form.is_valid():
            form.save()
            return redirect('portefolio:disciplinas')
    else:
        form = AreaCientificaForm(instance=areaCientifica)
    context = {'form': form, 'areaCientifica': areaCientifica}
    return render(request, 'portefolio/edita_areaCientifica.html', context)

@login_required
def edita_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    if request.POST:
        form = DocenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('portefolio:disciplinas')
    else:
        form = DocenteForm(instance=docente)
    context = {'form': form, 'docente': docente}
    return render(request, 'portefolio/edita_docente.html', context)

@login_required
def edita_linguagemProgramacao_view(request, linguagemProgramacao_id):
    linguagemProgramacao = LinguagemProgramacao.objects.get(id=linguagemProgramacao_id)
    if request.POST:
        form = LinguagemProgramacaoForm(request.POST or None, instance=linguagemProgramacao)
        if form.is_valid():
            form.save()
            return redirect('portefolio:disciplinas')
    else:
        form = LinguagemProgramacaoForm(instance=linguagemProgramacao)
    context = {'form': form, 'linguagemProgramacao': linguagemProgramacao}
    return render(request, 'portefolio/edita_linguagemProgramacao.html', context)



@login_required
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('portefolio:cursos')

@login_required
def apaga_areaCientifica_view(request, areaCientifica_id):
    areaCientifica = AreaCientifica.objects.get(id=areaCientifica_id)
    areaCientifica.delete()
    return redirect('portefolio:disciplinas')

@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('portefolio:disciplinas')

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('portefolio:projetos')

@login_required
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('portefolio:disciplinas')

@login_required
def apaga_linguagemProgramacao_view(request, linguagemProgramacao_id):
    linguagemProgramacao = LinguagemProgramacao.objects.get(id=linguagemProgramacao_id)
    linguagemProgramacao.delete()
    return redirect('portefolio:disciplinas')











