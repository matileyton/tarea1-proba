from cmath import log
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from tabulate import tabulate

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
#Europa
p_eu=[]
c_eu=[]

for x in dic:
    if x['continente']== 'Europe':
        p_eu.append(x['pais'])
        c_eu.append(int(x['casos']))

ma = max(c_eu)
mi = min(c_eu)
n = len(c_eu)
rango = ma - mi
ni= 1 + 3.32*log(n,10)
i = rango/6
i = round(i)

i1=[mi, mi+i]
i2=[mi+i, mi+2*i]
i3=[mi+2*i, mi+3*i]
i4=[mi+3*i, mi+4*i]
i5=[mi+4*i, mi+5*i]
i6=[mi+5*i, ma]
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

x=[str(i1),str(i2),str(i3),str(i4),str(i5),str(i6)]
y=[c1,c2,c3,c4,c5,c6]

plt.bar(x,y)
plt.xticks(rotation=90)

plt.title("Grafico de frecuencia por intervalo casos por millon en Europa")
plt.show()
plt.close

fre=[
    ['1',str(i1),c1],
    ['2',str(i2),c2],
    ['3',str(i3),c3],
    ['4',str(i4),c4],
    ['5',str(i5),c5],
    ['6',str(i6),c6]
]

i=0
n = len(c_eu)

for x in fre:
    i += x[2]
    x.append(i)
    x.append(x[2]/n)
    x.append(i/n)


# print (tabulate(fre, headers=['N° Intervalo','Intervalo','Frecuencia', 'Frecuencia Absoluta','Frecuencia Relativa','Frecuencia Relativa Absoluta']))

#Latinoamerica y el Caribe
p_las=[]
c_las=[]

for x in dic:
    if x['continente']== 'Latin America and the Caribbean':
        p_las.append(x['pais'])
        c_las.append(int(x['casos']))


ma = max(c_las)
mi = min(c_las)
n = len(c_las)
rango = ma - mi
ni= 1 + 3.32*log(n,10)
i = rango/7
i = round(i)

i1=[mi, mi+i]
i2=[mi+i+1, mi+2*i]
i3=[mi+2*i+1, mi+3*i]
i4=[mi+3*i+1, mi+4*i]
i5=[mi+4*i+1, mi+5*i]
i6=[mi+5*i+1, mi+6*i]
i7=[mi+6*i+1, ma]

c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0

for x in c_las:
    if x>= i7[0]:
        c7+=1
    elif x>= i6[0]:
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

x=[str(i1),str(i2),str(i3),str(i4),str(i5),str(i6),str(i7)]
y=[c1,c2,c3,c4,c5,c6,c7]

plt.bar(x,y)
plt.xticks(rotation=90)

plt.title("Grafico de frecuencia por intervalo casos por millon en Latinoamerica y el Caribe")
plt.show()
plt.close

fre=[
    ['1',str(i1),c1],
    ['2',str(i2),c2],
    ['3',str(i3),c3],
    ['4',str(i4),c4],
    ['5',str(i5),c5],
    ['6',str(i6),c6],
    ['7',str(i7),c7]
]

i=0
n = len(c_las)

for x in fre:
    i += x[2]
    x.append(i)
    x.append(x[2]/n)
    x.append(i/n)


# print (tabulate(fre, headers=['N° Intervalo','Intervalo','Frecuencia', 'Frecuencia Absoluta','Frecuencia Relativa','Frecuencia Relativa Absoluta']))
