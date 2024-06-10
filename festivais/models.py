from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome_localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_localizacao

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    info = models.TextField()
    imagem = models.ImageField(null=True, blank=True)
    bandas = models.ManyToManyField(Banda)
    posicao = models.ManyToManyField(Localizacao)

    def __str__(self):
        return self.nome
