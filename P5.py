from cmath import log, sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

'''
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
fre=[
    ['1',i1,c1],
    ['2',i2,c2],
    ['3',i3,c3],
    ['4',i4,c4],
    ['5',i5,c5],
    ['6',i6,c6]
]

i=0
n = len(c_eu)

for x in fre:
    i += x[2]
    x.append(i)
    x.append(x[2]/n)
    x.append(i/n)
    x.append((x[1][0] + x[1][1])/2)



print (tabulate(fre, headers=['N° Intervalo','Intervalo','Frecuencia', 'Frecuencia Absoluta','Frecuencia Relativa','Frecuencia Relativa Absoluta','Marca de clase']))


medes=[
    ['Media',311032],
    ['Moda',311032],
    ['Varianza'],
    ['Desviacion Estandar'],
    ['Coeficiente de Sesgo']
]
vari=[]
for x in fre:
    vari.append([x[6],x[2]])



medes[2].append(np.var(vari))
medes[3].append(np.std(vari))
medes[4].append((1/1-n)*((vari[0][0]-medes[0][1])**3+(vari[1][0]-medes[0][1])**3+(vari[2][0]-medes[0][1])**3+(vari[3][0]-medes[0][1])**3+(vari[4][0]-medes[0][1])**3+(vari[5][0]-medes[0][1])**3)/(np.std(vari))**3)

print (tabulate(medes, headers=['Medida Descriptivas','Resultado']))





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

fre=[
    ['1',i1,c1],
    ['2',i2,c2],
    ['3',i3,c3],
    ['4',i4,c4],
    ['5',i5,c5],
    ['6',i6,c6],
    ['7',i7,c7]
]

i=0
n = len(c_las)

for x in fre:
    i += x[2]
    x.append(i)
    x.append(x[2]/n)
    x.append(i/n)
    x.append((x[1][0] + x[1][1])/2)


print (tabulate(fre, headers=['N° Intervalo','Intervalo','Frecuencia', 'Frecuencia Absoluta','Frecuencia Relativa','Frecuencia Relativa Absoluta','Marca de clase']))

medes=[
    ['Media',150946],
    ['Moda',32287],
    ['Varianza'],
    ['Desviacion Estandar'],
    ['Coeficiente de Sesgo']
]
varo=[]
for x in fre:
    varo.append([x[6],x[2]])



medes[2].append(np.var(varo))
medes[3].append(np.std(varo))
medes[4].append((1/1-n)*((varo[0][0]-medes[0][1])**3+(varo[1][0]-medes[0][1])**3+(varo[2][0]-medes[0][1])**3+(varo[3][0]-medes[0][1])**3+(varo[4][0]-medes[0][1])**3+(varo[5][0]-medes[0][1])**3+(varo[6][0]-medes[0][1])**3)/(np.std(vari))**3)

print (tabulate(medes, headers=['Medida Descriptivas','Resultado']))