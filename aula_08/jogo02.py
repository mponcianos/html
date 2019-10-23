from random import randint

num = randint(1, 100)
ganhou = False
xtentativas = 0

while ganhou==False:
    tentativa = input("Qual o número sorteado entre 1 e 100? ")
    xtentativas += 1

    if tentativa.isnumeric():
        tentativa = int(tentativa)
        if tentativa == num:
            print('Acertou!!!')
            ganhou=True
            continue
        elif tentativa > num:
            print('Tente número menor')
            continue
        elif tentativa < num:
            print('Tente número maior')
            continue
        else:
            continue
    else:
        print('meu irmão, só número por favor')
        continue

print('Número de tentativas: ', xtentativas)