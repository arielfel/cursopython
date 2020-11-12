# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:48:31 2020

@author: ariel
"""

import pandas as pd
import requests
import io
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
enlace = 'https://raw.githubusercontent.com/python-unsam/UNSAM_2020c2_Python/master/Notas/10_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))
ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(data_lyp[['longitud']], data_lyp['peso']) # ajusto el modelo
grilla_x = np.linspace(start = 0, stop = 30, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))
data_lyp.plot.scatter('longitud','peso')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()
#%%
#Coeficiente, para saber la pendiente de la recta
print(ajus.coef_)
#Peso específico = 7.19988996
#%% Error cuadrático medio
errores = data_lyp.peso - (ajus.predict(data_lyp[['longitud']]))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio
