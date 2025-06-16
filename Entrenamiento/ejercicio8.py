"""
📝 Ejercicio: Calcular promedio, nota más alta y más baja
Tienes una lista de notas de un estudiante. Escribe un programa en Python que:

Calcule la suma total de las notas

Calcule el promedio

Encuentre la nota más alta

Encuentre la nota más baja"""

notas = [8.5, 9.0, 10.0, 7.5, 9.5]

suma = sum(notas)
print(f"Esta es la suma total de las notas:",float(suma))

cantidad = len(notas)
promedio = suma/cantidad
print(f"Esta es el promedio de las notas: {promedio}")

nota_alta = max(notas)
print(f"Esta es la nota más alta:{nota_alta}")

nota_baja = min(notas)
print(f"Esta es la nota más baja:{nota_baja}")


