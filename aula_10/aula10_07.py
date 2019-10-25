from bs4 import BeautifulSoup
import urllib.request
import requests

def CarregaPagina(url, codin='utf-8'):
    session = requests.Session()
    session.headers.update(
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0)'})
    with session.get(url) as response:
        html = response.content
    return BeautifulSoup(html, 'html.parser')

""" PESQUISA URL """
url = input("Digite sua URL para pesquisa: http://")
url = url.lower()

conta_url = 0

prefixo = "http://"
url = prefixo + url

print()
print("Pesquisando LINKS em " + url)
print()

pagina = CarregaPagina(url)
#req = requests.get(url)
#pagina = BeautifulSoup(req.text, 'html.parser')

for link in pagina.find_all('a'):
    print(link.get('href'))
    conta_url += 1

print(conta_url)