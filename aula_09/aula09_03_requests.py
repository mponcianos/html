# CONSUMINDO API
import requests
import json
ler_cep = input('Informe o CEP: ')

req = requests.get("https://viacep.com.br/ws/{}/json/".format(ler_cep))

print(req.json())
json.loads(req.text)
