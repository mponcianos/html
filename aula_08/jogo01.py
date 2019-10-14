"""
@author: Ponciano
"""
from random import randint

num = randint(1, 100)
ganhou = False
xtentativas = 0

while (ganhou == False):
    tentativa = input('Qual o número sorteado? ')
    xtentativas +=1
    if tentativa.isnumeric():
        tentativa = int(tentativa)
        if tentativa == num:
            print('Acertou!!!!')
            ganhou = True
        elif tentativa > num:
            print('Tente número menor')
            continue
        elif tentativa < num:
            print('Tente número MAIOR')
            continue
        else:
            continue

    else:
        print('só número por favor')
        continue

print('Você realizou %i tentativas' %xtentativas)