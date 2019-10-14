import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil').text

pagina = BeautifulSoup(website_url, 'parser.html')

table = pagina.find('table',  {'class':'wikitable sortable'})

table = pagina.find('tbody')
print(table)



links = table.find_all('a')

uf = []

for i in links:
    uf.append(i.get('title'))

for j in uf:
    print(j)