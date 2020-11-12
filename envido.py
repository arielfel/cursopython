
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:07:36 2020

@author: ariel
"""
#Estos ejercicios los hicimos en conjunto con Ivan Felsztyna
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def envido():
    repartida = random.sample(naipes,k=3)
    cartas_1a7 = [1,2,3,4,5,6,7]
    cartas_10a12 = [10,11,12]
    palos_iguales = []
    ord_palos_iguales = []
    cartas_envido = []
    for i in range(1):
        if repartida[i][1] == repartida[i+1][1] and repartida[i][1] == repartida[i+2][1]:
            if repartida[i][0] in cartas_1a7 and repartida[i+1][0] in cartas_1a7 and repartida[i+2][0] in cartas_1a7:
                palos_iguales.append(repartida[i][0])
                palos_iguales.append(repartida[i+1][0])
                palos_iguales.append(repartida[i+2][0])
                ord_palos_iguales = sorted(palos_iguales)
                cartas_envido.append(ord_palos_iguales[1]+ord_palos_iguales[2]+20)
            elif repartida[i][0] in cartas_10a12 and repartida[i+1][0] in cartas_10a12 and repartida[i+2][0] in cartas_10a12:
                cartas_envido.append(20)
            elif repartida[i][0] in cartas_10a12 or repartida[i+1][0] in cartas_10a12 or repartida[i+2][0] in cartas_10a12:
                palos_iguales.append(repartida[i][0])
                palos_iguales.append(repartida[i+1][0])
                palos_iguales.append(repartida[i+2][0])
                ord_palos_iguales = sorted(palos_iguales)
                if ord_palos_iguales[1] in cartas_1a7:
                    cartas_envido.append(ord_palos_iguales[0]+ord_palos_iguales[1]+20)
                elif ord_palos_iguales[1] in cartas_10a12:
                    cartas_envido.append(ord_palos_iguales[0]+20)
        elif repartida[i][1] == repartida[i+1][1]:
            if repartida[i][0] in cartas_1a7 and repartida[i+1][0] in cartas_1a7:
                cartas_envido.append(repartida[i][0]+repartida[i+1][0]+20)
            elif repartida[i][0] in cartas_1a7 and repartida[i+1][0] in cartas_10a12:
                cartas_envido.append(repartida[i][0]+20)
            elif repartida[i][0] in cartas_10a12 and repartida[i+1][0] in cartas_1a7:
                cartas_envido.append(repartida[i+1][0]+20)
            else:
                cartas_envido.append(20)
        elif repartida[i][1] == repartida[i+2][1]:
            if repartida[i][0] in cartas_1a7 and repartida[i+2][0] in cartas_1a7:
                cartas_envido.append(repartida[i][0]+repartida[i+2][0]+20)
            elif repartida[i][0] in cartas_1a7 and repartida[i+2][0] in cartas_10a12:
                cartas_envido.append(repartida[i][0]+20)
            elif repartida[i][0] in cartas_10a12 and repartida[i+2][0] in cartas_1a7:
                cartas_envido.append(repartida[i+2][0]+20)
            else:
                cartas_envido.append(20)
        elif repartida[i+1][1] == repartida[i+2][1]:
            if repartida[i+1][0] in cartas_1a7 and repartida[i+2][0] in cartas_1a7:
                cartas_envido.append(repartida[i+1][0]+repartida[i+2][0]+20)
            elif repartida[i+1][0] in cartas_1a7 and repartida[i+2][0] in cartas_10a12:
                cartas_envido.append(repartida[i+1][0]+20)
            elif repartida[i+1][0] in cartas_10a12 and repartida[i+2][0] in cartas_1a7:
                cartas_envido.append(repartida[i+2][0]+20)
            else:
                cartas_envido.append(20)
        else:
            cartas_envido.append(0)
    return cartas_envido

def envido_alto(lista):
    return lista[0] >= 31

N = 1000000
G = sum([envido_alto(envido()) for i in range(N)])
prob = G/N
print(f'Repartí {N} veces, de las cuales {G} saqué envido de 31, 32 ó 33.')
print(f'Podemos estimar que la probabilidad de sacar envido mayor o igual a 31 es de {prob:.6f}.')
#Con un N de 1000000:
#La probabilidad de envido = 31 es 0.029833
#La probabilidad de envido = 32 es 0.014915
#La probabilidad de envido = 33 es 0.015474
#La probabilidad de envido >= 31 es 0.060100