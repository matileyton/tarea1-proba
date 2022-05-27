import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Punto 1
    df = pd.read_csv("COVID-19 Coronavirus.csv")
    dCasesForMillion=df.nlargest(20, "Tot Cases//1M pop")

    plt.bar(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Total Cases"].tolist())
    plt.xticks(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Country"].tolist(), rotation=80)
    plt.xlabel("Paises")
    plt.ylabel("Casos totales de COVID")
    plt.title("Casos totales de COVID por país")
    plt.show()
    plt.close

    plt.bar(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Tot Cases//1M pop"].tolist())
    plt.xticks(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Country"].tolist(), rotation=80)
    plt.xlabel("Paises")
    plt.ylabel("Casos de Covid por Millon")
    plt.title("Cantidad de Casos por Millon por País")
    plt.show()
    plt.close()

    #Punto 2

