#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mponcianos
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('planilha.xls')
dados = df.sort_values(by="VALOR")

dados["DESTINO_NOME"].value_counts().plot.barh()

plt.show()
