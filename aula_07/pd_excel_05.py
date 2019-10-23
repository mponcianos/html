#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import pandas as pd
df = pd.read_excel('planilha.xls')

valor = df.sort_values(by="VALOR")
print(valor)

print (valor["DESTINO_NOME"].unique())

print(valor["DESTINO_NOME"].value_counts())
