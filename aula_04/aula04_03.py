# MÓDULO DA DIVISÃO
def modulo(x1):
    mod = (x1 % 2)
    return mod

a = int(input('Informe um numero:'))

mod2 = modulo(a)

if mod2>0:
    print('O número %i é impar' %a)
else:
    print('o número par é', a)

