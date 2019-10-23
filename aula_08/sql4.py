# Em discurso há um discurso
# e duas coleções de palavras
# sem significado "stop words":
# sw e stop_w

from discurso import discurso, sw2

aux = discurso

# letras minusculas
aux = aux.lower()

# retirar pontuação
for i in '.,:;!?*"%0123456789“”':
     aux = aux.replace(i,"")

# separando palavras
aux2 = aux.split()

# criando um dicionário
palavras = dict()

for i in aux2:
    if i not in palavras:
        palavras[i] = 1
    else:
        palavras[i] += 1

# excluindo as palavras sem significado
for i in sw2:
    if i in palavras.keys():
        palavras.pop(i)
    else:
        continue

import sqlite3 as sql

conexao = sql.connect('banco_dados1.db')
aux = conexao.cursor()

#sq1 = '''CREATE TABLE palavra_discurso (
#                                discurso  TEXT,
#                                palavra   TEXT,
#                                ocorrencia  REAL);'''

#aux.execute(sq1)

sq2 = '''INSERT INTO palavra_discurso VALUES
         ("ONU", ?, ? )'''

for i in palavras.keys():
    aux.execute(sq2, (i,palavras[i]))


conexao.commit()

