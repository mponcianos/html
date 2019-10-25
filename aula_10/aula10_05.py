from bs4 import BeautifulSoup
import requests

#url = "www25.senado.leg.br/web/senadores/em-exercicio"
url = 'pf.gov.br'

prefixo = "http://"
url = prefixo + url

pagina = requests.get(url)
page = BeautifulSoup(pagina.text, 'html.parser')

s1 = page.find_all('div')

print(s1)
print(len(s1))

"""
for i in s1:
    print(i.text)








s2 = page.find_all('p')[1].get_text()
print(s2)
"""