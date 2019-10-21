# MOSTRAR PARES E IMPARES MENOR QUE 10
x = 0

while x < 10:
    print('impar' if (x % 2) else 'par')
    print('impar {}'.format(x) if (x % 2) else 'par %i' % x)
    x+=1
