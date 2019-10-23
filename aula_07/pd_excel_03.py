#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import pandas as pd
df = pd.read_excel('planlha.xls')

valor = df.sort_values(by="VALOR")
print(valor)

print(valor.loc[1:1])


df.dtypes

df["VALOR"]
valor["VALOR"]

