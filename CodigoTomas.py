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

covid = {'Country' : archivo['Country'].tolist() ,
        'Other names': archivo['Other names'].tolist(),
        'Code': archivo['ISO 3166-1 alpha-3 CODE'].tolist(),
        'Population': archivo['Population'].tolist(),
        'Continent': archivo['Continent'].tolist(),
        'Total Cases': archivo['Total Cases'].tolist(),
        'Casos Totales x 1M': archivo['Casos Totales x 1M'].tolist(),
        'Muertes Totales x 1M': archivo['Muertes Totales x 1M'].tolist(),
        'Death percentage': archivo['Death percentage'].tolist()}

print(covid)


