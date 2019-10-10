import sqlite3 as sql

# criando uma conexão com banco_dados1
conexao = sql.connect("banco_dados1.db")

# criar um cursor aux  para interagir com o
# banco_dados1.db

aux = conexao.cursor()

# lendo os dados da tabela 1
sq1 = '''SELECT *
         FROM tabela_1 ;'''
aux.execute(sq1)

registros = aux.fetchall()

for i in registros:
    print(i)

# encerra a conexao

conexao.close()


