# NÚMERO PAR OU ÍMPAR
def modulo(x1):
    kana = (x1 % 2)
    return kana

a = int(input('Informe um numero:'))

mod2 = modulo(a)

if mod2 > 0:
    print('o numero é impar')
else:
    print('O numero é par')
