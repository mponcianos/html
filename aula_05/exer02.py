# ALGORITIMO MAIOR MENOR DE IDADE
idade = int(input('Informe sua idade:'))

if idade < 12:
    print('Desculpa 2x, criança na área')
elif idade <18 :
     print('Desculpa, de menor')
elif idade > 40 and idade < 60:
    print('ola idoso')
else:
    print('vá pra casa')
