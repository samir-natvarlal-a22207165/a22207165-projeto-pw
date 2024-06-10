from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario, Avaliacao, Categoria, Autor
from .forms import ArtigoForm, ComentarioForm, AvaliacaoForm, CategoriaForm, AutorForm
from django.contrib.auth.decorators import login_required

def lista_artigos(request):
    context = {
        'artigos': Artigo.objects.all(),
    }
    return render(request, 'artigos/lista_artigos.html', context)

def detalhes_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo)
    avaliacoes = Avaliacao.objects.filter(artigo=artigo)
    return render(request, 'artigos/detalhes_artigo.html', {'artigo': artigo, 'comentarios': comentarios, 'avaliacoes': avaliacoes})

@login_required
def novo_autor_view(request):
    form = AutorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')
    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')
    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def novo_categoria_view(request):
    form = CategoriaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')
    context = {'form': form}
    return render(request, 'artigos/novo_categoria.html', context)

@login_required
def novo_avaliacao_view(request):
    form = AvaliacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')
    context = {'form': form}
    return render(request, 'artigos/novo_avaliacao.html', context)

@login_required
def novo_comentario_view(request):
    form = ComentarioForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_artigos')
    context = {'form': form}
    return render(request, 'artigos/novo_comentario.html', context)

@login_required
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = AutorForm(instance=autor)
    context = {'form': form, 'autor':autor}
    return render(request, 'artigos/edita_autor.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = ArtigoForm(instance=artigo)
    context = {'form': form, 'artigo':artigo, 'autores': autores, 'categorias': categorias}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def edita_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.POST:
        form = ComentarioForm(request.POST or None, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = ComentarioForm(instance=comentario)
    context = {'form': form, 'comentario':comentario}
    return render(request, 'artigos/edita_comentario.html', context)

@login_required
def edita_categoria_view(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.POST:
        form = CategoriaForm(request.POST or None, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = CategoriaForm(instance=categoria)
    context = {'form': form, 'categoria':categoria}
    return render(request, 'artigos/edita_categoria.html', context)

@login_required
def edita_avaliacao_view(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    if request.POST:
        form = AvaliacaoForm(request.POST or None, request.FILES, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    context = {'form': form, 'avaliacao':avaliacao}
    return render(request, 'artigos/edita_avaliacao.html', context)

@login_required
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:lista_artigos')

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos:lista_artigos')

@login_required
def apaga_categoria_view(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    categoria.delete()
    return redirect('artigos:lista_artigos')

@login_required
def apaga_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('artigos:lista_artigos')

@login_required
def apaga_avaliacao_view(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    avaliacao.delete()
    return redirect('artigos:lista_artigos')

