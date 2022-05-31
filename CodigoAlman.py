import pandas as pd
import matplotlib.pyplot as plt

#CSV
archivo = pd.read_csv('COVID-19 Coronavirus.csv')
archivo = archivo.dropna()

#MODIFICAR NOMBRE COLUMNAS 7 & 8
archivo = archivo.rename(columns={f'{archivo.columns.values[7]}':'Casos Totales x 1M'})
archivo = archivo.rename(columns= {f'{archivo.columns.values[8]}':'Muertes Totales x 1M'})

#GRAFICO 2

muertestotales = archivo['Total Deaths'].tolist()
continentes = archivo['Continent'].tolist()
poblacion = archivo['Population'].tolist()

filtrocontinentes = []
filtromt = {}
filtropb = {}

for x in range(220):
    if continentes[x] not in filtrocontinentes:
        filtromt[f'{continentes[x]}'] = 0
        filtropb[f'{continentes[x]}'] = 0
        filtrocontinentes.append(continentes[x])

    filtromt[f'{continentes[x]}'] += muertestotales[x]
    filtropb[f'{continentes[x]}'] += poblacion[x]

fmhc = []
for y in filtrocontinentes:
    fmhc.append(((filtromt[y]/filtropb[y]) * 1000000))

'''
plt.bar(filtrocontinentes, fmhc)
plt.xlabel('Continentes')
plt.xticks(rotation = 90)
plt.ylabel('Cantidad de fallecidos por millon de Habitantes')
plt.title('GRAFICO 2')
plt.show()
plt.close()
''' 

plt.boxplot(fmhc)
plt.show()

mpmpc = {'mpm': fmhc, 'continentes': filtrocontinentes}
mpmpcdf = pd.DataFrame(mpmpc)

boxplot = mpmpcdf.boxplot(column=['mpm'])
boxplot.plot()

fig, ax = plt.subplots(figsize=(12, 8))
grafico = archivo.boxplot(by = 'Continent', column=[archivo.columns.values[8]], grid = True, ax=ax, rot=90)
grafico.set_ylabel('Muertes x Millon de Personas')
grafico.plot()
plt.show()
plt.close()
"""
dataframe = {}
for z in range(len(filtrocontinentes)):
    dataframe[f'{filtrocontinentes[z]}'] = fmhc[z]

print(dataframe)
df = pd.DataFrame()
boxplot = df.boxplot(column=['Col1'])
""" 

#GRAFICO 3
casos = archivo['Casos Totales x 1M'].tolist()
muertos = archivo['Muertes Totales x 1M'].tolist()
plt.scatter(casos, muertos)
plt.xlabel('Casos Totales por millon de Habitantes')
plt.ylabel('Cantidad de fallecidos por millon de Habitantes')
plt.title('GRAFICO 3')
plt.show()
plt.close()