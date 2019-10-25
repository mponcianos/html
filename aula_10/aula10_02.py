from bs4 import BeautifulSoup
import requests

url = "http://www.pf.gov.br/institucional/resolucao-no-04-" \
      "csp-dpf-de-26-de-marco-de-2015"
pag = requests.get(url)
soup = BeautifulSoup(pag.text,'html.parser')

pegadiv = soup.find("div", { "id" : "parent-fieldname-text" })

#print(pegadiv)
#print('----------------------------------------------------------')
#print(pegadiv.text)
arq = open('codigo-de-etica.txt', 'w')
arq.write(pegadiv.text)
arq.close()


