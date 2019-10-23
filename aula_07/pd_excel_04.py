#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import pandas as pd
df = pd.read_excel('planilha.xls')

valor = df.sort_values(by="VALOR")

print (valor[(valor["VALOR"] > 100000) & (valor["VALOR"] < 500000)])
