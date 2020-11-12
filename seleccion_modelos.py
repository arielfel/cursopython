# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:26:44 2020

@author: ariel
"""
import numpy as np
from sklearn import linear_model
np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática
x = indep_vars
y = dep_vars
def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X
def AIC(k, ecm, num_params):
    '''Calcula el AIC de una regresión lineal múltiple de 'num_params' parámetros, ajustada sobre una muestra de 'k' elementos, y que da lugar a un error cuadrático medio 'ecm'.'''
    aic = k * np.log(ecm) + 2 * num_params
    return aic
x8 = pot(x,8)
x1 = x.reshape(-1,1)
x2 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1)),axis=1)
x3 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1),x8[:,2].reshape(-1,1)),axis=1)
x4 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1),x8[:,2].reshape(-1,1),x8[:,3].reshape(-1,1)),axis=1)
x5 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1),x8[:,2].reshape(-1,1),x8[:,3].reshape(-1,1),x8[:,4].reshape(-1,1)),axis=1)
x6 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1),x8[:,2].reshape(-1,1),x8[:,3].reshape(-1,1),x8[:,4].reshape(-1,1),x8[:,5].reshape(-1,1)),axis=1)
x7 = np.concatenate((x.reshape(-1,1),x8[:,1].reshape(-1,1),x8[:,2].reshape(-1,1),x8[:,3].reshape(-1,1),x8[:,4].reshape(-1,1),x8[:,5].reshape(-1,1),x8[:,6].reshape(-1,1)),axis=1)
#Error Polinomio Grado 1
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x1,dep_vars)
errores_x1 = dep_vars - (lm_multiple.predict(x1))
ecm1 = (errores_x1**2).mean()
aic1 = AIC(50, ecm1, 2)
print('Grado del Polinomio: 1')
print('Cantidad de parametros: 2')
print(f'ECM: {ecm1}')
print(f'AIC: {aic1}')
print('----------')
#Error polinomio grado 2
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x2,dep_vars)
errores_x2 = dep_vars - (lm_multiple.predict(x2))
ecm2 = (errores_x2**2).mean()
aic2 = AIC(50, ecm2, 3)
print('Grado del Polinomio: 2')
print('Cantidad de parametros: 3')
print(f'ECM: {ecm2}')
print(f'AIC: {aic2}')
print('----------')
#Error polinomio grado 3
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x3,dep_vars)
errores_x3 = dep_vars - (lm_multiple.predict(x3))
ecm3 = (errores_x3**2).mean()
aic3 = AIC(50, ecm3, 4)
print('Grado del Polinomio: 3')
print('Cantidad de parametros: 4')
print(f'ECM: {ecm3}')
print(f'AIC: {aic3}')
print('----------')
#Error polinomio grado 4
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x4,dep_vars)
errores_x4 = dep_vars - (lm_multiple.predict(x4))
ecm4 = (errores_x4**2).mean()
aic4 = AIC(50, ecm4, 5)
print('Grado del Polinomio: 4')
print('Cantidad de parametros: 5')
print(f'ECM: {ecm4}')
print(f'AIC: {aic4}')
print('----------')
#Error polinomio grado 5
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x5,dep_vars)
errores_x5 = dep_vars - (lm_multiple.predict(x5))
ecm5 = (errores_x5**2).mean()
aic5 = AIC(50, ecm5, 6)
print('Grado del Polinomio: 5')
print('Cantidad de parametros: 6')
print(f'ECM: {ecm5}')
print(f'AIC: {aic5}')
print('----------')
#Error polinomio grado 6
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x6,dep_vars)
errores_x6 = dep_vars - (lm_multiple.predict(x6))
ecm6 = (errores_x6**2).mean()
aic6 = AIC(50, ecm6, 7)
print('Grado del Polinomio: 6')
print('Cantidad de parametros: 7')
print(f'ECM: {ecm6}')
print(f'AIC: {aic6}')
print('----------')
#Error polinomio grado 7
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x7,dep_vars)
errores_x7 = dep_vars - (lm_multiple.predict(x7))
ecm7 = (errores_x7**2).mean()
aic7 = AIC(50, ecm7, 8)
print('Grado del Polinomio: 7')
print('Cantidad de parametros: 8')
print(f'ECM: {ecm7}')
print(f'AIC: {aic7}')
print('----------')
#Error polinomio grado 8
lm_multiple = linear_model.LinearRegression()
lm_multiple.fit(x8,dep_vars)
errores_x8 = dep_vars - (lm_multiple.predict(x8))
ecm8 = (errores_x8**2).mean()
aic8 = AIC(50, ecm8, 9)
print('Grado del Polinomio: 8')
print('Cantidad de parametros: 9')
print(f'ECM: {ecm8}')
print(f'AIC: {aic8}')
print('----------')
#el minimo AIC es en grado 2

