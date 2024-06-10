from portefolio.models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente


def disciplinas_do_primeiro_ano():
    return Disciplina.objects.filter(ano=1).values_list('nome', flat=True)

def disciplinas_do_segundo_ano():
    return Disciplina.objects.filter(ano=1).values_list('nome', flat=True)

def disciplinas_do_terceiro_ano():
    return Disciplina.objects.filter(ano=3).values_list('nome', flat=True)

def disciplinas_do_primeiro_semestre():
    return Disciplina.objects.filter(semestre=1).values_list('nome', flat=True)

def disciplinas_do_segundo_semestre():
    return Disciplina.objects.filter(semestre=2).values_list('nome', flat=True)

def disciplinas_comecadas_com_S():
    return Disciplina.objects.filter(nome__istartswith='S').values_list('nome', flat=True)

def quantidade_disciplinas_com_ects_seis():
    return Disciplina.objects.filter(ects=6).count()

def disciplinas_com_ects_seis():
    return Disciplina.objects.filter(ects=6)

def disciplinas_com_menos_de_seis_ects():
    return Disciplina.objects.filter(ects__lt=6)

# filtros com parametro

def disciplinas_por_ano(ano):
    return Disciplina.objects.filter(ano=ano).values_list('nome', flat=True)

def disciplinas_por_semestre(semestre):
    return Disciplina.objects.filter(semestre=semestre).values_list('nome', flat=True)

def disciplinas_por_letra_inicial(letra):
    return Disciplina.objects.filter(nome__istartswith=letra).values_list('nome', flat=True)

def quantidade_disciplinas_com_ects(ects):
    return Disciplina.objects.filter(ects=ects).count()

def disciplinas_com_ects(ects):
    return Disciplina.objects.filter(ects=ects).values_list('nome', flat=True)

def disciplinas_com_menos_de_ects(ects):
    return Disciplina.objects.filter(ects__lt=ects)




