# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:54:45 2020

@author: ariel
"""
import copy
import numpy as np
import random
import matplotlib.pyplot as plt
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return comparaciones
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
            comparaciones += comp
    return comparaciones
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1
    lista[j] = v
    return comparaciones
a = ord_insercion([454, 997, 751, 325, 707, 623, 300, 891, 579, 539])
#%%
def ord_burbujeo(lista):
    n = len(lista)
    comparaciones = 0
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if lista[i+1] < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[1]
                cambio = True
        comparaciones += n - 1
        n -= 1
    return comparaciones
#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_merge
    return lista_nueva, comparaciones
def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones_aux = 0
    while(i < len(lista1) and j < len(lista2)):
        comparaciones_aux += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, comparaciones_aux
#%%
def generar_lista(N):
    lista = []
    for i in range(N):
        numero = random.randint(1,1000)
        lista.append(numero)
    return lista
#%%
lista_de_listas = []
for i in range(1,257):
    lista = generar_lista(i)
    lista_de_listas.append(lista)
#%%
lista_1 = copy.deepcopy(lista_de_listas)
lista_2 = copy.deepcopy(lista_de_listas)
lista_3 = copy.deepcopy(lista_de_listas)
lista_4 = copy.deepcopy(lista_de_listas)
comp_seleccion = []
for lista in lista_1:
    comparaciones = ord_seleccion(lista)
    comp_seleccion.append(comparaciones)
comp_insercion = []
for lista in lista_2:
    comparaciones = ord_insercion(lista)
    comp_insercion.append(comparaciones)
comp_burbujeo = []
for lista in lista_3:
    comparaciones = ord_burbujeo(lista)
    comp_burbujeo.append(comparaciones)
comp_merge_sort = []
for lista in lista_4:
    comparaciones = merge_sort(lista)[1]
    comp_merge_sort.append(comparaciones)
comparaciones_seleccion = np.array(comp_seleccion)
#promedio_seleccion = np.mean(array_seleccion)
comparaciones_insercion = np.array(comp_insercion)
#promedio_insercion = np.mean(array_insercion)
comparaciones_burbujeo = np.array(comp_burbujeo)
#promedio_burbujeo = np.mean(array_burbujeo)
comparaciones_merge_sort = np.array(comp_merge_sort)
#%%
eje_x = np.linspace(1,256,num=256)
plt.figure()
linea_seleccion = plt.plot(eje_x,comparaciones_seleccion, label = "Selección")
linea_insercion = plt.plot(eje_x,comparaciones_insercion, label = "Inserción")
linea_burbujeo = plt.plot(eje_x,comparaciones_burbujeo, label = "Burbujeo")
linea_merge_sort = plt.plot(eje_x,comparaciones_merge_sort, label = "Merge_sort")
plt.title("Comparaciones por Método de Ordenamiento")
plt.xlabel("Largo de la lista")
plt.ylabel("Número de comparaciones")
plt.legend()
plt.show()