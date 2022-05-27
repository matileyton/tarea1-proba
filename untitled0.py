# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:03:35 2021

@author: Matías
"""

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import math
from matplotlib.ticker import PercentFormatter

df=pd.read_csv("disney_plus_titles.csv")

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df["Year"]=df["date_added"].dt.year

d1 = df[df["type"] == "TV Show"]
d2 = df[df["type"] == "Movie"]

d12 = d1[d1.Year==2019]
d22 = d2[d2.Year==2019]

d13 = d1[d1.Year==2020]
d23 = d2[d2.Year==2020]

d14 = d1[d1.Year==2021]
d24 = d2[d2.Year==2021]

ctvshows=[d12.shape[0],d13.shape[0],d14.shape[0]]
cmovies=[d22.shape[0],d23.shape[0],d24.shape[0]]

ndg=len(ctvshows)
ib=np.arange(ndg)
ab=0.35

pt.bar(ib, ctvshows, width=ab, label="TV Shows")
pt.bar(ib+ab, cmovies, width=ab, label="Movies")
pt.legend(loc="best")

pt.xticks(ib+ab, ("2019", "2020", "2021"))

pt.ylabel("Número de Elementos")
pt.xlabel("Año")
pt.title("Cantidad de Elementos que fueron agregados cada año")

pt.show()
pt.close()

dr1=d1[d1.release_year==2010]
dr2=d2[d2.release_year==2010]

dr12=d1[d1.release_year==2011]
dr22=d2[d2.release_year==2011]

dr13=d1[d1.release_year==2012]
dr23=d2[d2.release_year==2012]

dr14=d1[d1.release_year==2013]
dr24=d2[d2.release_year==2013]

dr15=d1[d1.release_year==2014]
dr25=d2[d2.release_year==2014]

dr16=d1[d1.release_year==2015]
dr26=d2[d2.release_year==2015]

dr17=d1[d1.release_year==2016]
dr27=d2[d2.release_year==2016]

dr18=d1[d1.release_year==2017]
dr28=d2[d2.release_year==2017]

dr19=d1[d1.release_year==2018]
dr29=d2[d2.release_year==2018]

dr11=d1[d1.release_year==2019]
dr21=d2[d2.release_year==2019]

dr112=d1[d1.release_year==2020]
dr212=d2[d2.release_year==2020]

dr113=d1[d1.release_year==2021]
dr213=d2[d2.release_year==2021]

rtvshows=[dr1.shape[0],dr12.shape[0],dr13.shape[0],dr14.shape[0],dr15.shape[0],dr16.shape[0],dr17.shape[0],dr18.shape[0],dr19.shape[0],dr11.shape[0]+ctvshows[0],dr112.shape[0]+ctvshows[1],dr113.shape[0]+ctvshows[2]]
rmovies=[dr2.shape[0],dr22.shape[0],dr23.shape[0],dr24.shape[0],dr25.shape[0],dr26.shape[0],dr27.shape[0],dr28.shape[0],dr29.shape[0],dr21.shape[0]+cmovies[0],dr212.shape[0]+cmovies[1],dr213.shape[0]+cmovies[2]]

ndg=len(rtvshows)
ib=np.arange(ndg)
ab=0.35

pt.bar(ib, rtvshows, width=ab, label="TV Shows")
pt.bar(ib+ab, rmovies, width=ab, label="Movies")
pt.legend(loc="best")

pt.xticks(ib+ab, ("2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"))

pt.ylabel("Número de Elementos")
pt.xlabel("Año")
pt.title("Año de Lanzamiento de cada Elemento")

pt.show()
pt.close()

eumo=0
eutv=0
otmo=0
ottv=0

for n in range(1368):
    if "United States" in str(df["country"][n]) and "Movie" in str(df["type"][n]):
       eumo +=1
    if "United States" in str(df["country"][n]) and "TV Show" in str(df["type"][n]):
        eutv +=1
    if "Movie" in str(df["type"][n]):
       otmo +=1
    if "TV Show" in str(df["type"][n]):
       ottv +=1

otmo=otmo-eumo
ottv=ottv-eutv

Movies=[eumo,otmo]
Tvshow=[eutv,ottv]

ndg=len(Movies)
ib=np.arange(ndg)
ab=0.35

pt.bar(ib, Movies, width=ab, label="Movies")
pt.bar(ib+ab, Tvshow, width=ab, label="TV Shows")
pt.legend(loc="best")

pt.xticks(ib+ab, ("Hechas en EEUU", "Hechas fuera de EEUU"))

pt.ylabel("Número de Elementos")
pt.xlabel("Lugar de Producción")
pt.title("Lugar de Producción")

pt.show()
pt.close()

dmov=df[df["type"] == "Movie"]
dmov=dmov.reset_index()
diff=[]
duración=[]
num=dmov["duration"].str.extract("(\d+(?:\.\d+)?)")

for n in range(991):
    resta=abs(float(dmov["release_year"][n])-float(dmov["Year"][n]))
    diff.append(resta)
    minuto=int(num[0][n])
    duración.append(minuto)


    
dtvg=df[df["rating"]=="TV-G"]
dtvgm=dtvg[dtvg["type"]=="Movie"]
dtvgm=dtvgm.reset_index()
num=dtvgm["duration"].str.extract("(\d+(?:\.\d+)?)")
Películas=[]
Minutos=[]

for n in range(224):
    minuto=int(num[0][n])
    Minutos.append(minuto)

pt.scatter(range(224), Minutos, label="TV-G")

dtvpg=df[df["rating"]=="TV-PG"]
dtvpgm=dtvpg[dtvpg["type"]=="Movie"]
dtvpgm=dtvpgm.reset_index()
num=dtvpgm["duration"].str.extract("(\d+(?:\.\d+)?)")
Películass=[]
Minutoss=[]

for n in range(165):
    minutoo=int(num[0][n])
    Minutoss.append(minutoo)

pt.scatter(range(165), Minutoss, label="TV-PG")
pt.legend(loc="best")
pt.ylabel("Minutos")
pt.xlabel("Número de Películas")
pt.title("Duración de Películas")

pt.show()
pt.close()

def tabla_de_frecuencia(lista):
    ni= round(1+(3.32*math.log10(len(lista))))
    R = max(lista)-min(lista)
    i= round(R/ni)
    R1=ni*i

    r=list(range(min(lista),max(lista)+1))
    cc=[]
    ll=[]
    contador=0

    for n in r:
        cc.append(n)
        contador+=1
        if contador==ni:
            ll.append(cc)
            cc=[]
            contador=0
        
    fr=[]
    for n in range(len(ll)):
        fr.append(0)
    c=0
    chan=[]
    while c<len(ll):
        for n in lista:
            if n in ll[c]:
                chan.append(n)
                fr[c]=len(chan)
        chan=[]
        c+=1

    pf=[]
    for n in fr:
        p= round((n/len(lista))*100, 0)
        pf.append(p)

    fra=[]
    for n in range(len(ll)):
        fra.append(0)
    c=0
    cchan=[]
    while c < len(ll):
        for n in lista:
            if n in ll[c]:
                cchan.append(n)
                fra[c]=len(cchan)
        c += 1

    pfra=[]
    for n in fra:
        pp= round((n/len(lista))*100,0)
        pfra.append(pp)

    tdf=pd.DataFrame()
    tdf["Valor"]=ll
    tdf["f"]=fr
    tdf["fr(%)"]=pf
    tdf["F"]=fra
    tdf["F(%)"]=pfra
    return tdf

dmovies=df[df["type"]=="Movie"]
products = pd.Series(dmovies.listed_in.values.flatten())
dcomedy = products[products.str.contains("Comedy")]

indice=list(dcomedy.index.values)
dcomedy=dmovies.drop(dmovies.index[indice])

indice1=list(dcomedy.index.values)
dcomedy1=df.drop(df.index[indice1])

dcomedy=dcomedy1[dcomedy1["type"]=="Movie"]
dcomedy=dcomedy.reset_index()
numm=dcomedy["duration"].str.extract("(\d+(?:\.\d+)?)")

Minutosss=[]

for n in range(379):
    minuto=int(numm[0][n])
    Minutosss.append(minuto)

tdfc=tabla_de_frecuencia(Minutosss)
print(tdfc)
pt.scatter(range(379), Minutosss, label="Comedy")
pt.legend(loc="best")


products = pd.Series(dmovies.listed_in.values.flatten())
dfamily = products[products.str.contains("Family")]

indice=list(dfamily.index.values)
dfamily=dmovies.drop(dmovies.index[indice])

indice1=list(dfamily.index.values)
dfamily1=df.drop(df.index[indice1])

dfamily=dfamily1[dfamily1["type"]=="Movie"]
dfamily=dfamily.reset_index()
nummm=dfamily["duration"].str.extract("(\d+(?:\.\d+)?)")

Minutossss=[]

for n in range(506):
    minuto=int(nummm[0][n])
    Minutossss.append(minuto)

tdff=tabla_de_frecuencia(Minutossss)
print(tdff)
pt.scatter(range(506), Minutossss, label="Family")
pt.legend(loc="best")
pt.ylabel("Minutos")
pt.xlabel("Número de Películas")
pt.title("Duración de Películas")

pt.show()
pt.close()

tdfc["cumpercentage"]=tdfc["f"].cumsum()/tdfc["f"].sum()*100

fig, ax=pt.subplots()
ax.bar(tdfc.index, tdfc["f"])
ax2=ax.twinx()
ax2.plot(tdfc.index, tdfc["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())
pt.xticks(range(0,14,1))

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
ax.set_xlabel("Intervalos")
ax.legend()

pt.title("Gráfico Tabla de Frecuencia Comedy")
pt.show()
pt.close()

tdff["cumpercentage"]=tdff["f"].cumsum()/tdff["f"].sum()*100

fig, ax=pt.subplots()
ax.bar(tdff.index, tdff["f"])
ax2=ax.twinx()
ax2.plot(tdff.index, tdff["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())
pt.xticks(range(0,18,1))

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
ax.set_xlabel("Intervalos")
ax.legend()

pt.title("Gráfico Tabla de Frecuencia Family")
pt.show()
pt.close()









