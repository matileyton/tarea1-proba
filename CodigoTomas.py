from cmath import log
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

dic=[]
for x in range(len(casos)):
    dic.append({'pais':paises[x], 'continente':continente[x],'casos':casos[x] })

tabla_europa=[]
p_eu=[]
c_eu=[]

for x in dic:
    if x['continente']== 'Europe':
        p_eu.append(x['pais'])
        c_eu.append(x['casos'])

max = max(c_eu)
min = min(c_eu)
print(min,max)
n = len(c_eu)
rango = max - min
ni= 1 + 3.32*log(n,10)
i = rango/6
print(rango , ni , i)
i = round(i)

i1=[min, min+i]
i2=[min+i, min+2*i]
i3=[min+2*i, min+3*i]
i4=[min+3*i, min+4*i]
i5=[min+4*i, min+5*i]
i6=[min+5*i, max]
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0

for x in c_eu:
    if x>= i6[0]:
        c6+=1
    elif x>= i5[0]:
        c5+=1
    elif x>= i4[0]:
        c4+=1
    elif x>= i3[0]:
        c3+=1
    elif x>= i2[0]:
        c2+=1
    elif x>= i1[0]:
        c1 +=1
print(c1,c2,c3,c4,c5,c6)
print(n)
print(c1+c2+c3+c4+c5+c6)