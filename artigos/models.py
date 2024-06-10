from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.usuario.username

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_destaque = models.ImageField(upload_to='artigos/', null=True, blank=True)

    def __str__(self):
        return f"{self.autor.usuario.username} tem este artigo {self.titulo} veja mais informação dentro dele"

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.artigo.titulo}"

class Avaliacao(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Avaliação de {self.autor.username} para {self.artigo.titulo}: {self.rating}"







