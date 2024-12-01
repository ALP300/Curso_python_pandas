# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:07:38 2024

@author: aitor
"""

import pandas as pd
import numpy as np
datos={'Nombre':['Leo','Aldair','IngeDJ','Rodri','Jeferson'],
       'Calificaciones':['9','13','14','15','20'],
       'Deportes':['Ajedrez','Básquet','natación','fútbol','balón mano'],
       'Materias':['Matemáticas','Métodos numéricos','cocina','Educación Física','Física']
       }
df= pd.DataFrame(datos)
print(df)
print('\n'*4)
datos2={'Nombre':['N/A','Aldair','Aldair','Rodri','Jeferson'],
       'Calificaciones':['9','13',np.nan,'15','20'],
       'Deportes':['N/A','Básquet','natación','fútbol','balón mano'],
       'Materias':['Matemáticas','N/A','cocina','Educación Física','Física']
       }

df2= pd.DataFrame(datos2)
print(df2)
print('\n'*4)
#ESTADÍSTICAS BÁSICAS
print(df2.info())
print('\n'*4)
print(df2.describe())

print('\n'*4)
nuevo= pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo)
nuevo.info()
print('\n'*4)
nuevo2= pd.DataFrame(df2)
nuevo2.dropna(how='any', inplace=True)
print(nuevo2)

print('\n'*4)
columna= df2[df2['Nombre']!='N/A']
print(columna)
print('\n'*4)
print(df2.head())



