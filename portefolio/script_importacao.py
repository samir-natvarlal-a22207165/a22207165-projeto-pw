from portefolio.models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente
import json

def importar_curso(ficheiro_json):
    with open(ficheiro_json, 'r') as file:
        data = json.load(file)

        # Import cursos
        for curso_data in data['cursos']:
            curso, created = Curso.objects.get_or_create(
                nome=curso_data['nome'],
                apresentacao=curso_data['apresentacao'],
                objetivos=curso_data['objetivos'],
                competencias=curso_data['competencias']
            )

        # Import areas cientificas
        for area_cientifica_data in data['areas_cientificas']:
            AreaCientifica.objects.get_or_create(nome=area_cientifica_data['nome'])

        # Import disciplinas
        for disciplina_data in data['disciplinas']:
            curso = Curso.objects.get(nome=disciplina_data['curso'])
            area_cientifica = AreaCientifica.objects.get(nome=disciplina_data['area_cientifica'])
            Disciplina.objects.get_or_create(
                nome=disciplina_data['nome'],
                ano=disciplina_data['ano'],
                semestre=disciplina_data['semestre'],
                ects=disciplina_data['ects'],
                curricularIUnitReadableCode=disciplina_data['curricularIUnitReadableCode'],
                curso=curso,
                area_cientifica=area_cientifica
            )

        # Import projetos
        for projeto_data in data['projetos']:
            disciplina = Disciplina.objects.get(nome=projeto_data['disciplina'])
            Projeto.objects.get_or_create(
                nome_projeto=projeto_data['nome_projeto'],
                descricao=projeto_data['descricao'],
                conceitos_aplicados=projeto_data['conceitos_aplicados'],
                tecnologias_usadas=projeto_data['tecnologias_usadas'],
                disciplina=disciplina
            )

        # Import linguagens de programacao
        for linguagem_data in data['linguagens_programacao']:
            LinguagemProgramacao.objects.get_or_create(nome=linguagem_data['nome'])

        # Import docentes
        for docente_data in data['docentes']:
            docente, created = Docente.objects.get_or_create(nome=docente_data['nome'])
            for disciplina_name in docente_data['disciplinas']:
                disciplina = Disciplina.objects.get(nome=disciplina_name)
                docente.disciplinas.add(disciplina)






