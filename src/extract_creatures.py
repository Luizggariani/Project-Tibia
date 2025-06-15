##Extrair dados da API

import requests

def get_creatures_data():
    url = "https://api.tibiadata.com/v4/creatures"
    response = requests.get(url)

    if response.status_code == 200:
        creatures_data = response.json()['creatures']['creature_list']
        return creatures_data
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []
