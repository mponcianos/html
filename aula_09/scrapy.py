import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'

website_url = requests.get(url)

print(website_url.status_code)

pagina = website_url.text


pagina_final = BeautifulSoup(pagina, 'html.parser')

print(pagina_final.prettify())

table = pagina_final.find('table', {'class':'wikitable sortable'})

links = table.find_all('a')

pais = []

for i in links:
    pais.append(i.get_text('a'))

for i in pais:
    print(i)