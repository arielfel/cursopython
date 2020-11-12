# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:52:16 2020

@author: ariel
"""

#%% 6.10
import numpy as np
import matplotlib.pyplot as plt
def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()
N = 100000
fig = plt.figure()
ax1 = plt.subplot(2, 1, 1)
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.ylim(-1000,1000)
ax1.title.set_text('12 caminatas al azar')
lista = [] #Guarda los 12 arrays en lista y grafica las 12 caminatas
for i in range(12):
    i = randomwalk(N)
    plt.plot(i)
    lista.append(i)
maximos = [] # Guarda los maximos valores absolutos de cada array
for array in lista:
    maximo = max(abs(array))
    maximos.append(maximo)
def busca_maximo(lista):
    '''
    Devuelve la posición del valor máximo de una lista desordenada
    '''
    pos = 0
    maximo = 0
    i = 0
    while i <= (len(lista)-1):
        if lista[i] > maximo:
            maximo = lista[i]
            pos = i
        i += 1
    return pos
def busca_minimo(lista):
    '''
    Devuelve la posición del valor mínimo de una lista desordenada
    '''
    pos = 0
    minimo = lista[0]
    i = 0
    while i <= (len(lista)-1):
        if lista[i] < minimo:
            minimo = lista[i]
            pos = i
        i += 1
    return pos
ax2 = plt.subplot(2, 2, 3)
plt.plot(lista[busca_maximo(maximos)]) #Grafica el array que corresponde al
                                       #que tiene el valor absoluto más alto.
                                       #Sería el que más se aleja del origen
ax2.title.set_text('La caminata que más se aleja')
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.ylim(-1000,1000)
ax3 = plt.subplot(2, 2, 4)
plt.plot(lista[busca_minimo(maximos)])#Grafica el array que corresponde al
                                       #que tiene el valor absoluto más bajo.
                                       #Sería el que menos se aleja del origen
ax3.title.set_text('La caminata que menos se aleja')
plt.xticks([])
plt.yticks([])
plt.ylim(-1000,1000)
plt.show()
