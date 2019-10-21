# CONTAR PAR OU IMPAR MENOR QUE 10
x = 0

while x < 10:
    if x%2 > 0:
        print('{} é ímpar'.format(x))
    else:
        print('{} é par'.format(x))
    x+=1
