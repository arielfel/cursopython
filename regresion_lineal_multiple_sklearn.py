# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:34:41 2020

@author: ariel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]
data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})
X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)
ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)
errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio
#Preguntas:
#A mayor superficie, mayor precio.
#A mayor antiguedad, menor precio.
#La ordenada al origen vale 7.714781491002601.