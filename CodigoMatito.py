import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("COVID-19 Coronavirus.csv")
    dCasesForMillion=df.nlargest(20, "Tot Cases//1M pop")
    casesForCountry=[]
    countries=[]
    for country in dCasesForMillion["Country"]:
        countries.append(country)
    for casesInCountry in dCasesForMillion["Total Cases"]:
        casesForCountry.append(casesInCountry)

    plt.bar(np.arange(len(countries)), casesForCountry)

    plt.xticks(np.arange(len(countries)), countries, rotation=80)
    plt.xlabel("Paises")
    plt.ylabel("Casos totales de COVID")
    plt.title("Casos totales de COVID por país")

    plt.show()
    plt.close