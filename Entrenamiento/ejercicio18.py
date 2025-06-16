import numpy as np 
"""
🧮 Ejercicio: Sistema de análisis de calificaciones de varios estudiantes
Crea un programa que:
Genere una matriz 5x4 con calificaciones aleatorias entre 0 y 10 de 5 estudiantes en 4 materias usando numpy.
Muestre la matriz con enumerate, donde cada fila representa un estudiante y cada columna una materia.
Calcule y muestre:
El promedio por estudiante
El promedio por materia
El estudiante con el mejor promedio
La materia con la nota más baja en total
Use zip() para mostrar el nombre del estudiante con sus notas."""
print("_____________________________________")
estudiantes = ["Ana", "Luis", "Pedro", "Sofía", "Carlos"]
materias = ["Matemáticas", "Lengua", "Ciencias", "Inglés"]

np.random.seed(1)
calificaciones = np.random.uniform(0,10,(5,4))

for i ,fila in enumerate(calificaciones):
    nombre = estudiantes[i]
    fila_redondeada =[f"{nota:.2f}" for nota in fila]
    print(f"{nombre}:{fila_redondeada}")
print("_____________________________________")
print("Promedio de las calificaciones: ")
promedio_estudiantes = np.mean(calificaciones, axis = 1)

for i, (e,promedio) in enumerate(zip(estudiantes, promedio_estudiantes), start=1):
    print(f"{e}: {promedio:.2f}")
print("_____________________________________")
print("Promedioo por todas las materias: ")
promedio_materia = np.mean(calificaciones, axis=0)
for i, (m,promedio) in enumerate(zip(materias,promedio_materia), start = 1):
    print(f"{m}: {promedio:.2f}")


