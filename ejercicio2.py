# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:35:46 2024

@author: aitor
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.info())
print(datos.head())
print(datos.iloc[0:5])
#Refiones salteados
print(datos.iloc[[0,3,3,6,23]])
#COLUMNAS
print(datos.iloc[:,0:3])
print(datos.iloc[[0,3,6,24],[0,5,6]])
print(datos.iloc[0:5,5:8])