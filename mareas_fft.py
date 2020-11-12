# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:15:54 2020

@author: ariel
"""

import pandas as pd

df = pd.read_csv('Data/OBS_SHN_SF-BA.csv',index_col=['Time'], parse_dates=True)#indexamos el DF con la primer columna (time)
df.head()
df['1-18-2014 9:00':'1-18-2014 18:00']
df['2-19-2014']
#%% Graficamos la serie temporal
df['12-25-2014':].plot()

df['10-15-2014':'12-15-2014'].plot()
