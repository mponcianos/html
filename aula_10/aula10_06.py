from bs4 import BeautifulSoup
import requests

""" PESQUISA URL """
url = input("Digite sua URL para pesquisa: http://")
url = url.lower()

conta_url = 0
prefixo = "http://"
url = prefixo + url

print()
print("Pesquisando LINKS em " + url)
print()

req = requests.get(url)
pagina = BeautifulSoup(req.text, 'html.parser')

for link in pagina.find_all('a'):
    print(link.get('href'))
    conta_url += 1

print(conta_url)
