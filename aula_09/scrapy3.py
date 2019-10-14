import requests

url = 'http://www.pf.gov.br/imprensa/noticias/2019/10/pf-desarticula-organizacao-criminosa-dedicada-a-pratica-de-crimes-contra-os-correios'

pag = requests.get(url)

pag1 = pag.text

print(pag.status_code)

#print (pag1)

from bs4 import BeautifulSoup

pagina = BeautifulSoup(pag1, 'html.parser')

dados = pagina.find_all('h1',  {'class':'documentFirstHeading'})

for i in dados:
    print (i.get_text())

