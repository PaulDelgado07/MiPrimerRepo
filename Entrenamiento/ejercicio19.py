"""Crea un programa que:
Genere una secuencia de tiempo con numpy.linspace() entre 0 y 2π.
Calcule los valores de una función seno para ese tiempo usando np.sin().
Calcule:
El valor máximo y mínimo de la función.
El promedio de la señal.
Muestra los resultados de forma tabular (usando enumerate si deseas).
(Opcional si usas librerías gráficas) Muestra un gráfico de la función seno."""

import numpy as np
import math

tiempo = np.linspace(0, 2*np.pi, 20)

senal = np.sin(tiempo)

print("⏱️ Señal sonoidal (seno):\n")
for i, (t, s) in enumerate(zip(tiempo,senal), start =2):
    print(f"{i}. t={t:.2f} -> sin(t) = {s:.2f}") 

print("Analisis de la señal. - ")
maxima_senal = np.max(senal)
print(f"🔺 Maximo valor: {maxima_senal:.2f}")
minima_senal = np.min(senal)
print(f"🔻 Minimo valor: {minima_senal:.2f}")
promedio_senal = np.mean(senal)
print(f"📉 Promedio: {promedio_senal:.2f}")