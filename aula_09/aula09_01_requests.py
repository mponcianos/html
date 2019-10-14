import requests

# LENDO PÁGINA
url = "https://www25.senado.leg.br/web/senadores/em-exercicio"

pag = requests.get(url)

print(pag.text)