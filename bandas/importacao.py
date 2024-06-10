from bandas.models import Banda, Album, Musica
import json

def importar_bandas(ficheiro_json):
    with open(ficheiro_json, 'r') as file:
        data = json.load(file)

        for banda_data in data['bandas']:
            banda_obj = Banda.objects.create(
                nome=banda_data['nome'],
                ano=banda_data['ano'],
                nacionalidade=banda_data['nacionalidade'],
                informacoes_variadas=banda_data['informacoes_variadas']
            )

            for album_data in banda_data['albuns']:
                album_obj = Album.objects.create(
                    banda=banda_obj,
                    titulo=album_data['nome']
                )

                for musica_data in album_data['musicas']:
                    Musica.objects.create(
                        album=album_obj,
                        titulo=musica_data['nome'],
                        ano=musica_data['ano'],
                        duracao=musica_data['duracao']
                    )
