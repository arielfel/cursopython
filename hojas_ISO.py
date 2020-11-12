# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:33:02 2020

@author: ariel
"""

def hoja(n):
    if n == 0:
        ancho = 841
        largo = 1189
        return (ancho, largo)
    elif n % 2 != 0:
        ancho = hoja(n - 1)[1] // 2
        largo = hoja(n - 1)[0]
        return (ancho, largo)
    else:
        ancho = hoja(n - 1)[1] // 2
        largo = hoja(n - 1)[0]
        return (ancho, largo)