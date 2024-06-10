from django.shortcuts import render, redirect
from bandas.models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm
from django.contrib.auth import authenticate, login, models, logout
from django.contrib.auth.decorators import login_required

def listaBandas_view(request):
    context = {
      'bandas': Banda.objects.all().order_by('nome'),
    }
    return render(request, "bandas/listaBandas.html", context)

def listaAlbuns_view(request):
    context = {
      'albuns': Album.objects.all().order_by('nome'),
    }
    return render(request, "bandas/listaAlbuns.html", context)

def listaMusicas_view(request):
    context = {
      'musicas': Musica.objects.all().order_by('nome'),
    }
    return render(request, "bandas/listaMusicas.html", context)

def album_view(request, album_id):
    context = {
      'album': Album.objects.get(id=album_id),
    }
    return render(request, 'bandas/album.html', context)

def musica_view(request, musica_id):
    context = {
      'musica': Musica.objects.get(id=musica_id),
    }
    return render(request, 'bandas/musica.html', context)

def banda_view(request, banda_id):
    context = {
      'banda': Banda.objects.get(id=banda_id),
    }
    return render(request, 'bandas/banda.html', context)

@login_required
def novo_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:listaBandas')
    context = {'form': form}
    return render(request, 'bandas/novo_banda.html', context)

@login_required
def novo_album_view(request):
    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:listaAlbuns')
    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@login_required
def novo_musica_view(request):
    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:listaMusicas')
    context = {'form': form}
    return render(request, 'bandas/novo_musica.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:listaBandas')
    else:
        form = BandaForm(instance=banda)
    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:listaAlbuns')
    else:
        form = AlbumForm(instance=album)
    context = {'form': form, 'album':album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:listaMusicas')
    else:
        form = MusicaForm(instance=musica)
    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:listaBandas')

@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:listaAlbuns')

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:listaMusicas')

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login_bandas')

    return render(request, 'bandas/registo_bandas.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'bandas/user_bandas.html')
        else:
            render(request, 'bandas/login_bandas.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login_bandas.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:listaBandas')



