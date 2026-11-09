# Anais Medina NC 0099 fecha 9 noviembre 2026

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problema 8: Dispositivos (Modelo, precio USD, incluye control remoto, memoria RAM GB)
chr = ['Chromecast HD', 29.99, True, 1.5]
frt = ['Fire TV Stick 4K', 49.99, True, 2.0]
rku = ['Roku Express', 24.99, True, 1.0]
app = ['Apple TV 4K', 129.00, True, 4.0]
nvd = ['Nvidia Shield', 199.99, True, 3.0]

# Creamos una lista de listas (corformando la tabla)
lista_dispositivos=[chr, frt, rku, app, nvd]
# print(lista_dispositivos)
#utilizar panda parab organizar la tabla (DataFrame)
# a cada columna le pones un nombre
df_dispositivos_tele=pd.DataFrame(lista_dispositivos, columns=["Nombre","Cantidad","Es_FB","Año"])
print(df_dispositivos_tele)
# creamos el archivo CSV y lo guardamos en CSV
# df_dispositivos_tele.to_csv("dispositivos_tele.csv", index=False)
# ahora creamremos una grafica de lineas 
# donde X es Nombre en el eje horinzontal
# donde Y es Cantidad en el eje vertical
plt.plot(df_dispositivos_tele["Nombre"],df_dispositivos_tele["Cantidad"]) 
plt.title("Grafica televisiones 0099")
plt.xlabel("Nombre de dispositivos televisivos")
plt.ylabel("Cantidad de usuarios")
plt.show()

# ceamos una grafica de puntos
plt.scatter(df_dispositivos_tele["Nombre"],df_dispositivos_tele["Cantidad"]) 
plt.show()

# grafica de barras 
plt.bar(df_dispositivos_tele["Nombre"],df_dispositivos_tele["Cantidad"]) 
plt.title("dispositivos 0099")
plt.xlabel("las televisiones")
plt.ylabel("Cantidad usuarios")
plt.show()

# ordena la grafica de barras de manera descendente
# de la mas grande a la pequeña
df_rs_ordenar=df_dispositivos_tele.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()

# coloreando la grafica 
df_rs_ordenar=df_dispositivos_tele.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# grafica de pastel
# plt.plot(df_dispositivos_tele["Nombre"],df_dispositivos_tele["Cantidad"])
plt.pie(df_dispositivos_tele["Cantidad"],labels=df_dispositivos_tele["Nombre"])
plt.show()

# Grafica de control remoto

plt.bar(df_dispositivos_tele["Modelo"], df_dispositivos_tele["Control_Remoto"])
plt.title("televisiones con control remoto 0099")
plt.xlabel("Modelo de televisiones")
plt.ylabel("Incluye control remoto")
plt.show()


# Grafica de memoria RAM

plt.bar(df_dispositivos_tele["Modelo"], df_dispositivos_tele["Memoria_RAM_GB"])
plt.title("Memoria RAM de televisiones 0099")
plt.xlabel("Modelo de televisiones")
plt.ylabel("Memoria RAM GB")
plt.show()


# Grafica de puntos de memoria RAM

plt.scatter(df_dispositivos_tele["Modelo"], df_dispositivos_tele["Memoria_RAM_GB"])
plt.title("Memoria RAM de televisiones 0099")
plt.xlabel("Modelo de televisioness")
plt.ylabel("Memoria RAM GB")
plt.show()