from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='band_photos/', null=True, blank=True)
    ano = models.IntegerField(default=1)
    nacionalidade = models.CharField(max_length=100, default = 'trocar')
    informacoes_variadas = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} pertence aos {self.banda.nome}'

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField(default=1)
    duracao = models.IntegerField(default=1)
    spotify_link = models.URLField(max_length=200, null=True, blank=True)
    letra = models.TextField(default='', null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.album.nome} -> {self.nome}'


