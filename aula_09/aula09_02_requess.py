import requests

url = "https://www25.senado.leg.br/web/senadores/em-exercicio"
#url = "https://www25.rcicio"

try:
    pag = requests.get(url)

    print(pag.text)
except Exception as e:
    print('Requisição com problema:', e)