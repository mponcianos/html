from random import randint

numero_gerado=randint(1,100)
print('O aplicativo gerou um número aleatório entre 0 e 100.')
print('O seu objetivo é descobrir que número é este.')
print('Vamos iniciar.')

tentativa=0
numeros=[]
numero_operador=999

while numero_operador!=numero_gerado:
    print('')
    numero_operador=input('Informe um número de 0 a 100 ')
    if numero_operador.isnumeric()==False:
        print('Digite apenas números.')
        continue
    numero_operador=int(numero_operador)
    numeros.append(numero_operador)
    if numero_operador<numero_gerado:
        print('O número',numero_operador,'é MENOR que o número procurado.')
    elif numero_operador>numero_gerado:
        print('O número', numero_operador, 'é MAIOR que o número procurado.')
#    for contador in numeros
#        print(contador,' - ',numeros)
    tentativa += 1

print('Você acertou o número',numero_gerado,'em',tentativa,'tentativas.')
print(numeros)
