"""
🧠 Ejercicio: Promedio de calificaciones
Enunciado:
1. Haz un programa en Python que:
2. Pida al usuario ingresar cuántas calificaciones va a ingresar.
3. Luego le pida esas calificaciones una por una.
4. Guarde las calificaciones en una lista.
Calcule y muestre el promedio de las calificaciones ingresadas.
"""
import math

"""calificaciones = []

cantidad = int(input("Ingrese la cantidad de calificaciones: "))

for i in range(cantidad): 
    notas = float(input("Ingrese las notas de los estudiantes: "))
    calificaciones.append(notas)

suma = sum(calificaciones)

promedio = suma/cantidad

print(f"Calificaciones ingresadas: {calificaciones}")

print(f"La suma de las calificaciones son: {suma:.2f}")
print(f"El promedio de las calificaciones son: {promedio:.2f} ")"""

grades = []

cuantity = int(input("enter the amount of grades: "))

for i in range(cuantity): 
    notes = float(input("Enter the grades of the studiands: "))
    grades.append(notes)

suma = sum(grades)
promedio = suma/cuantity
print(f"sum the grades is:{suma}")
print(f"average of the notes:{promedio}")





