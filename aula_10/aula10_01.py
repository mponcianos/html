from bs4 import BeautifulSoup
import requests

url = "https://www25.senado.leg.br/web/senadores/em-exercicio"
#url = "https://nostarch.com"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.text, 'html.parser')

#print(soup)
#print(soup.text)

#autores = soup.select('p')
#print(autores[0])

lista = soup.find("table")
#print(lista.prettify())

linhas = lista.find_all("tr")
for linha in linhas:
    print(linha.text)






"""
linhas = lista.find_all("tr")

for l1 in linhas:
    lin = l1.find_all("td")
    # print(len(lin))
    if len(lin) >= 3:
        nome = lin[0].text.strip()
        tele = lin[1].text.strip()
        rama = lin[2].text.strip()
        mail = lin[3].text.strip()
        matr = lin[4].text.strip()
        carg = lin[5].text.strip()
        registro = nome, tele, rama, mail, matr, carg
        print(registro)


"""