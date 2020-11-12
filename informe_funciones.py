# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:52:52 2020

@author: ariel
"""
import csv
from fileparse import parse_csv
#%%
def leer_camion (nombre_archivo): 
    camion = parse_csv(nombre_archivo,select=['nombre','cajones','precio'],types=[str,int,float])
    return camion
#%%
def leer_precios(nombre_archivo):
   precios = dict(parse_csv(nombre_archivo,types=[str,float], has_headers=False))
   return precios
#%%
def hacer_informe(camion,precios):
    lista = []
    for i,linea in enumerate(camion):
        tupla = (camion[i]['nombre'],camion[i]['cajones'],camion[i]['precio'],
        (precios[camion[i]['nombre']]- camion[i]['precio']))
        lista.append(tupla)
    return lista
#%%Ejercicio 5.1 
def imprimir_informe(lista):
    headers = ('Nombre', 'Cajones','Precio','Cambio')
    separadores = ('-------','--------','---------','---------')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{separadores[0]:>10s} {separadores[1]:>10s} {separadores[2]:>10s} {separadores[3]:>10s}')
    for nombre,cajones,precio,cambio in lista:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
#%% Ejercicio 5.2
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    imprimir = imprimir_informe(informe)
    return imprimir


        