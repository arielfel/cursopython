# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:50:11 2020

@author: ariel
"""
#Este ejercicio lo hicimos en conjunto con Ivan Felsztyna
#%%Ejercicio 4.7 Generala no servida
from collections import Counter
import random
def tirar():
    '''devuelve una lista con 5 numeros random simulando una tirada de dados de generala'''
    tirada_primera = []
    dados = Counter()
    mesa = []
    dados_no_iguales = []
    tirada_segunda = []
    tirada_tercera = []
    
    for i in range(5):
        tirada_primera.append(random.randint(1,6)) # itera sobre 5 numeros aleatorios y los apendea a la lista vacia
    
    for i, numero in enumerate(tirada_primera):
        dados[tirada_primera[i]] += 1 #cuenta la cantidad de veces qeu salió cada numero del dado
    
    dado_y_cantidad = dados.most_common(1)# elijo el dado que mas veces salió
    
    for i in range(dado_y_cantidad[0][1]):#itero sobre la lista que tiene los dados con mas repeticion
        mesa.append(dado_y_cantidad[0][0])#apendeo a la lista mesa
    
    dado_mas_comun = dado_y_cantidad[0][0]
    
    for numero in tirada_primera:#vuelvo a iterar sobre la primer tirada
        if numero != dado_mas_comun:#si los dados son distintos a los mas repetidos
            dados_no_iguales.append(numero)#apendeo a una lista de dados no iguales
    
    for i in range(len(dados_no_iguales)):#itero sobre los dados no iguales
        tirada_segunda.append(random.randint(1,6))#apendeo esos dados a una segunda tirada
    
    for numero in tirada_segunda:#itero sobre la segunda tirada 
        if numero == dado_mas_comun:#si el dado es igual al mas comuun, lo apendeo a la mesa
            mesa.append(numero)
    
    for i in range(5-len(mesa)):#itero sobre los dados que quedan despues de la segunda tirada
        tirada_tercera.append(random.randint(1,6))#los apendeo a la tercer tirada
    
    for i in tirada_tercera:#itero sobre la tercer tirada
        mesa.append(i)#apendeo a la mesa para tener todos los dados
    
    return mesa#me retorna la lista de los dados luego de 2 o 3 tiradas dependiendo si hice generala

def generala(lista):
    return min(lista) == max(lista)

generala_no_servida = generala(tirar())
N = 1000000
G = sum([generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')