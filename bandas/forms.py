from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        help_texts = {
            'nome': 'Insira o nome da banda.',
            'foto': 'Faça upload de uma foto da banda (opcional).',
            'ano': 'Insira o ano de formação da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda.',
            'informacoes_variadas': 'Insira informações variadas sobre a banda (opcional).'
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'banda': 'Selecione a banda a qual o álbum pertence.',
            'nome': 'Insira o nome do álbum.',
            'capa': 'Faça upload da capa do álbum (opcional).'
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        help_texts = {
            'album': 'Selecione o álbum ao qual a música pertence.',
            'nome': 'Insira o nome da música.',
            'ano': 'Insira o ano de lançamento da música.',
            'duracao': 'Insira a duração da música em segundos.',
            'spotify_link': 'Insira o link do Spotify para a música (opcional).',
            'letra': 'Insira a letra da música (opcional).',
            'biografia': 'Insira uma breve biografia (4-5 linhas) sobre a música (opcional).'
        }
