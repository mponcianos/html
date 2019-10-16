texto = 'Você está no curso de RI com Linguagem Python'
texto2 = 'Você;está;no;curso de RI com Linguagem Python'

print(texto.count('o'))
print(texto.find('curso'))

print(texto.split(' '))
print(len(texto.split(' ')))

print(texto2.split(';'))
print(id(texto.replace("curso","")))

print(id(texto))