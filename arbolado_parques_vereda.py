# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:02:51 2020

@author: ariel
"""

import pandas as pd
import os
import seaborn as sns
#%%
#Abre el dataframe de árboles en veredas
directorio = 'Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_veredas = pd.read_csv(fname)
#Abre el dataframe de árboles en parques
directorio = 'Data'
archivo = 'arbolado.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname)
#%%Seleccionamos las columnas de interes y las filas de los Tipas y generamos 2 nuevos dataframes
columnas = ['diametro', 'altura_tot']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][columnas].copy()
columnas_2 = ['diametro_altura_pecho', 'altura_arbol']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][columnas_2].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro", "altura_arbol": "altura_tot"})
#%%Agregamos 2 columnas nuevas en cada DF
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'
#%%unimos con concat los 2 dataframes con las mismas columnas
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
#%% Graficamos el boxplot de diamtero segun el ambiente
sns.boxplot(y = 'altura_tot',data = df_tipas, x = 'ambiente')
sns.boxplot(x = 'diametro',data = df_tipas, y = 'ambiente',palette='Set3',orient='h')
