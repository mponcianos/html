from random import randint

num = randint(1, 100)
ganhou = False
xtentativas = 0

while (ganhou==False):
    tentativa = input('Qual o número sorteado entre 1 e 10')
    xtentativas +=1

    if tentativa.isnumeric():
        x = int(tentativa)

        if x==num:
            print('GANHOU!!!!!!')
            ganhou=True
        elif x>num:
            print('Digite um número menor')
        elif x<num:
            print('Digite um número maior')

    else:
         print('Meu irmão, só número por favor')
         continue

print('Você realizou %i tentativas' %xtentativas)