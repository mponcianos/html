#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='curso',password='123',db='db_exemplo')
cursor = conn.cursor()
cursor.execute("select uf,qtd from tabela1 where codigo=1 group by uf")
linhas = cursor.fetchall()

import pandas as pd
df = pd.DataFrame( [[ij for ij in i] for i in linhas] )
df.rename(columns={0: 'UF', 1: 'QTD'}, inplace=True);

print(df)

X = df['UF'];
y = df['QTD'];

import matplotlib.pyplot as plt 
plt.plot(X,y)
plt.title('Vendas X Estado')
plt.xlabel('Estados')
plt.ylabel('Qtd. de vendas')
plt.show()


