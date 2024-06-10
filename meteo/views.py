from django.shortcuts import render
import requests


def index_view(request):
    global_id = 1110600 # id de Lisboa
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
    response = requests.get(url)
    data = response.json()
    url = "https://api.ipma.pt/open-data/distrits-islands.json"
    response = requests.get(url)

    if response.status_code == 200:
        localidades = response.json().get('data', [])
        localidades_lista = [
            {"id": localidade['globalIdLocal'], "nome": localidade['local']}
            for localidade in localidades
        ]
    else:
        localidades_lista = []

    nome = ""
    for localidade in localidades_lista:
        if localidade['id'] == global_id:
            nome = localidade['nome']
            break

    for day in data['data']:
        if(day["idWeatherType"] >= 10):
            day["idWeatherType"] = "meteo/w_ic_d_" + str(day["idWeatherType"]) + ".svg"
        else:
            day["idWeatherType"] = "meteo/w_ic_d_0" + str(day["idWeatherType"]) + ".svg"

    context = {
        'city': nome,
        'weather': data['data'],
        'localidades': localidades_lista,
        'id': int(1110600),
    }

    return render(request, "meteo/index.html", context)

def city_dia_view(request, id, dia):
    global_id = id  # ID para Lisboa
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
    response = requests.get(url)
    data = response.json()

    url = "https://api.ipma.pt/open-data/distrits-islands.json"
    response = requests.get(url)

    if response.status_code == 200:
        localidades = response.json().get('data', [])

        localidades_lista = [
            {"id": localidade['globalIdLocal'], "nome": localidade['local']}
            for localidade in localidades
        ]

        nome = ""
        for localidade in localidades_lista:
            if localidade['id'] == id:
                nome = localidade['nome']
                break
    else:
        localidades_lista = []
        nome = ""

    if(data['data'][dia]["idWeatherType"] >= 10):
        data['data'][dia]["idWeatherType"] = "meteo/w_ic_d_" + str(data['data'][dia]["idWeatherType"]) + ".svg"
    else:
        data['data'][dia]["idWeatherType"] = "meteo/w_ic_d_0" + str(data['data'][dia]["idWeatherType"]) + ".svg"

    context = {
        'city': nome,
        'day': data['data'][dia],
        'dia':dia,
        'filename': data['data'][dia]["idWeatherType"],
        'localidades': localidades_lista,
        'id': id,
    }

    return render(request, "meteo/day.html", context)


def city_view(request, id):
    global_id = id  # ID para Lisboa
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id}.json"
    response = requests.get(url)
    data = response.json()


    url = "https://api.ipma.pt/open-data/distrits-islands.json"

    # Fazendo a requisição GET
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        localidades = response.json().get('data', [])  # Acessa a chave 'data' se existir
        localidades_lista = [
            {"id": localidade['globalIdLocal'], "nome": localidade['local']}
            for localidade in localidades
        ]
    else:
        localidades_lista = []

    nome = ""
    for localidade in localidades_lista:
        if localidade['id'] == id:
            nome = localidade['nome']
            break

    for day in data['data']:
        if(day["idWeatherType"] >= 10):
            day["idWeatherType"] = "meteo/w_ic_d_" + str(day["idWeatherType"]) + ".svg"
        else:
            day["idWeatherType"] = "meteo/w_ic_d_0" + str(day["idWeatherType"]) + ".svg"

    context = {
        'city': nome,
        'weather': data['data'],
        'localidades': localidades_lista,
        'id': int(id),
    }

    return render(request, "meteo/index.html", context)











