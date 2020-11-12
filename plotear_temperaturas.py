# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:06:37 2020

@author: ariel
"""
import matplotlib.pyplot as plt
import numpy as np

def graficar():
    np.load('../Data/Temperaturas.npy')
    return plt.hist(temperaturas,bins=30)
