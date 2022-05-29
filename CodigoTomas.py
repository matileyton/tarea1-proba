from tkinter import N
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

'''
(4) Genere una tabla de frecuencia para la cantidad de casos por mill ́on de habitantes para el continente europeo,
junto con su gr ́afico de cantidades respectivo. Haga un proceso similar, pero ahora para Latinoamerica y el
Caribe. Comente (y compare) los resultados destacando algo de inter ́es.

(5) Con respecto a lo hecho en el ejercicio (4), btenga las principales medidas descriptivas de la variable “Casos
por Mill ́on de habitantes”¿C ́omo es la simetrtriaa de la variable? Comente (y compare) los resultados destacando
algo de inter ́es.
'''
#CSV
archivo = pd.read_csv('COVID-19 Coronavirus.csv')

#MODIFICAR NOMBRE COLUMNAS 7 & 8
archivo = archivo.rename(columns={f'{archivo.columns.values[7]}':'Casos Totales x 1M'})
archivo = archivo.rename(columns= {f'{archivo.columns.values[8]}':'Muertes Totales x 1M'})

#P4
casos = archivo['Casos Totales x 1M'].tolist()
paises = archivo['Country'].tolist()
continente = archivo['Continent'].tolist()
#print(len(casos), len(paises), len(continente))
dic=[]
for x in range(len(casos)):
    dic.append({'pais':paises[x], 'continente':continente[x],'casos':casos[x] })
tabla_europa=[]
tabla_europa.append(['Pais','Casos'])
for x in dic:
    
    if x['continente']== 'Europe':
        tabla_europa.append([x['pais'] , x['casos']])

for i in tabla_europa:
        print(i[0],i[1])
    
