import requests

url = 'https://www25.senado.leg.br/web/senadores/em-exercicio'

pag = requests.get(url)

pag1 = pag.text

print(pag.status_code)

print (pag1)

from bs4 import BeautifulSoup

pagina = BeautifulSoup(pag1, 'html.parser')

dados = pagina.find_all('td',  {'class':'break-word'})

for i in dados:
    print (i.get_text())

