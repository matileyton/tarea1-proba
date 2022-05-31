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
#print(len(casos), len(paises), len(continente))
dic=[]
for x in range(len(casos)):
    dic.append({'pais':paises[x], 'continente':continente[x],'casos':casos[x] })

tabla_europa=[]
p_eu=[]
c_eu=[]
tabla_europa.append(['Pais','Casos'])


for x in dic:
    if x['continente']== 'Europe':
        tabla_europa.append([x['pais'] , x['casos']])
        p_eu.append(x['pais'])
        c_eu.append(x['casos'])


'''
for i in tabla_europa:
        print(i[0],i[1])
'''

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


print(i1,i2,i3,i4,i5,i6)



'''  
plt.bar(p_eu,c_eu)
plt.xticks(np.arange(len(p_eu)), p_eu, rotation=80)
plt.xlabel("Paises de Europa")
plt.ylabel("Casos de Covid por Millon")
plt.title("Cantidad de Casos por Millon en Europa")
plt.show()
plt.close()

tabla_las=[]
p_las=[]
c_las=[]
tabla_las.append(['Pais','Casos'])

for x in dic:
    if x['continente']== 'Latin America and the Caribbean':
        tabla_las.append([x['pais'] , x['casos']])
        p_las.append(x['pais'])
        c_las.append(x['casos'])

for i in tabla_las:
        print(i[0],i[1])

plt.bar(p_las,c_las)
plt.xticks(np.arange(len(p_las)), p_las, rotation=80)
plt.xlabel("Paises de Latinoamerica y el Caribe")
plt.ylabel("Casos de Covid por Millon")
plt.title("Cantidad de Casos por Millon en Latinoamerica y el Caribe")
plt.show()
plt.close()

'''