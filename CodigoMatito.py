import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("COVID-19 Coronavirus.csv")
    dCasesForMillion=df.nlargest(20, "Tot Cases//1M pop")

    plt.bar(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Total Cases"].tolist())
    plt.xticks(np.arange(len(dCasesForMillion["Country"].tolist())), dCasesForMillion["Country"].tolist(), rotation=80)
    plt.xlabel("Paises")
    plt.ylabel("Casos totales de COVID")
    plt.title("Casos totales de COVID por país")
    plt.show()
    plt.close