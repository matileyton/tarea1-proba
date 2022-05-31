import pandas as pd
import matplotlib.pyplot as plt

#CSV
archivo = pd.read_csv('COVID-19 Coronavirus.csv')
archivo = archivo.dropna()

#MODIFICAR NOMBRE COLUMNAS 7 & 8
archivo = archivo.rename(columns={f'{archivo.columns.values[7]}':'Casos Totales x 1M'})
archivo = archivo.rename(columns= {f'{archivo.columns.values[8]}':'Muertes Totales x 1M'})

#GRAFICO 3
casos = archivo['Casos Totales x 1M'].tolist()
muertos = archivo['Muertes Totales x 1M'].tolist()
plt.scatter(casos, muertos)
plt.xlabel('Casos Totales por millon de Habitantes')
plt.ylabel('Cantidad de fallecidos por millon de Habitantes')
plt.title('GRAFICO 3')
plt.show()
plt.close()