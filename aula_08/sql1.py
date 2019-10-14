import sqlite3 as sql

# criando uma conexão com um banco de dados:
# método connect - faz conexão com o bd, caso
# não exista cria o banco de dados.

conexao = sql.connect("banco_dados1.db")

# criar um cursor aux  para interagir com o
# banco_dados1.db

aux = conexao.cursor()

# cria a tabela_1 por meio do método
# execute do cursor aux

sq1 = '''CREATE TABLE tabela_1 (
                                nome TEXT,
                                email TEXT,
                                peso  REAL);'''

# cria a tabela_1

aux.execute(sq1)

# confirma a operação

conexao.commit()

# encerra a conexao

conexao.close()