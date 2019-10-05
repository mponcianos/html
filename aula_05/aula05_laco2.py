# CONTAR PAR OU IMPAR MENOR QUE 10
x = 0

while x < 10:
    mod = (x%2)
    if mod > 0:
        print('%i é impar' %x)
    else:
        print('%i é par' %x)
    x+=1

