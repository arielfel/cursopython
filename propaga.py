# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:21:29 2020

@author: ariel
"""

# Ejercicio 3.9 Propagación
def propagar(lista):
    for i in range(0, (len(lista)-1)):
        if lista[i] == 1 and lista[i+1] == 0:
            lista[i+1] = 1
    for i in range(len(lista)-1, 0, -1):
        if lista[i] == 1 and lista[i-1] == 0:
           lista[i-1] = 1
    return lista

               
## Tuve que apoyarme en codigo de un compañere de slack para resolverlo. Gracias
