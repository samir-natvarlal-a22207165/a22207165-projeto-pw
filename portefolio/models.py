from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.curso}),{self.ano}º ano,{self.semestre}º semestre"

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projeto_imagens/',null=True, blank=True)
    video_youtube = models.URLField(null=True, blank=True)
    repositorio_github = models.URLField(null=True, blank=True)
    ficheiro_projeto = models.FileField(upload_to='ficheiros_projeto/', null=True, blank=True)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_projeto

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.ManyToManyField(Projeto, blank=True)
    disciplina = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=70)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome



