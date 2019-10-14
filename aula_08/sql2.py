import sqlite3 as sql

# criando uma conexão com banco_dados1

conexao = sql.connect("banco_dados1.db")

# criar um cursor aux  para interagir com o
# banco_dados1.db

aux = conexao.cursor()

# inserir dados na tabela tabela_1

sq1 = '''INSERT INTO tabela_1 (nome, email, peso)
values ('raucelio coelho cardoch valdes',
        'raucelio.rccv@dpf.gov.br',
        130  );'''
sq2 = '''INSERT INTO tabela_1 (nome, email, peso)
values ('ribson coelho cardoch valdes',
        'ribson.xxxx@xxx.xxx.dd',
        75  );'''

# inserir  tabela_1

aux.execute(sq1)
aux.execute(sq2)

# confirma a operação

conexao.commit()

# encerra a conexao

conexao.close()