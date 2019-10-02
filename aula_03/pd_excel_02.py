#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import pandas as pd
df = pd.read_excel('planilha.xls')

valor = df.loc[0:2, ["ORIGEM_NOME", "DESTINO_NOME", "VALOR"]]
print(valor)

