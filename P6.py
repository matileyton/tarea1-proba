import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Punto 6
    df = pd.read_csv("COVID-19 Coronavirus.csv")
    dCasesForContinent=df.groupby(by="Continent").sum()
    
    plt.pie(dCasesForContinent["Total Cases"].tolist(), labels = (dCasesForContinent.index.values.tolist()))
    plt.title("Casos totales por continente")
    plt.show()
    plt.close()