#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "https://www25.senado.leg.br/web/senadores/em-exercicio"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.text, 'html.parser')

lista = soup.find("table")

linhas = lista.find_all("tr")

"""
x = '----------------------------------------------------------'
for l1 in linhas:
    lin = l1.find_all("td")
    print(lin)
    print(x + str(len(lin)) + '\n')
"""
arq = open('senadores.txt', 'w')

for l1 in linhas:
    lin = l1.find_all("td")

    if len(lin) >= 3:
        nome = lin[0].text
        tele = lin[1].text.strip()
        rama = lin[2].text.strip()
        mail = lin[3].text.strip()
        matr = lin[4].text.strip()
        carg = lin[5].text.strip()
        registro = nome, tele, rama, mail, matr, carg
        print(registro)
        arq.write(str(registro)+'\n')

arq.close()
