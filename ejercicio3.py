# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:49:52 2024

@author: aitor
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.head())
datos.set_index("Location",inplace=True)
print("..................Melbourne..........")
print(datos.loc['Melbourne'])
print("..................Atlanta y Superficie..........")
print(datos.loc['Atlanta','Surface'] )