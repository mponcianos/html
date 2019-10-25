import requests
import json

requisicao = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/'
                          'versao/v1/odata/Moedas')
cotacao = json.loads(requisicao.text)

print(cotacao)
print(len(cotacao['value']))

x=0
while x < len(cotacao['value']):
    print(cotacao['value'][x])
    x+=1
