"""
🧾 Ejercicio: Registro de estudiantes y sus notas
Crea un programa que:

Le pida al usuario cuántos estudiantes va a registrar.

Para cada estudiante, le pida su nombre y sus 5 calificaciones.

Al final, muestre:

El nombre del estudiante.

Su lista de notas.

El promedio.

Una observación: “Aprobado” si el promedio es ≥ 7, “Reprobado” si es menor."""
estudiantes = {}

cantidad = int(input("-Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del estudiante ({i+1}): ")

    notas = []
    for j in range(5): 
        nota = float(input((f"Ingrese las calificaciones[{j+1}]: ")))
        notas.append(nota)

    estudiantes[nombre] = notas

print("\nLos resultados finales son: ")
for nombre, notas in estudiantes.items(): 
    promedio = sum(notas)/len(notas)
    estado = 'Aprobado' if promedio >= 7 else 'Reprobado'

    print(f"El nombre del estudiante: {nombre}")
    print(f"Lista de notas: {notas}")
    print(f"Este es tu pomedio: {promedio}")
    print(f"Estado : {estado}")

