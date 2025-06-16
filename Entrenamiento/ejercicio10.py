"""
🧾 Ejercicio: Consulta de calificaciones por estudiante
Crea un programa que:

Registre las calificaciones de varios estudiantes (nombre y 3 notas cada uno).

Guarde los datos en un diccionario.

Permita al usuario buscar a un estudiante por nombre y mostrar su promedio y estado (Aprobado o Reprobado).

Si el nombre no existe, que lo indique.
"""

estudiantes = {}

cantidad = int(input("Ingrese la cantidad de estudiantes que va a registrar: "))

for i in range(cantidad): 
    nombre = input(f"Ingrese el nombre del estudiante [{i+1}]: ")
    nombre_minuscula = nombre.lower()
    notas = [] 
    for j in range(3): 
        nota = float(input(f"Ingrese Las nota del estudiante [{i+1}]: "))
        notas.append(nota)

    estudiantes[nombre_minuscula] = notas 
print("______________________________________________")

buscado = input("Ingrese el nombre del estudiante: ")

if buscado in estudiantes: 
    estudiantes[nombre] = notas
    promedio = sum(notas)/len(notas)
    estado = 'Aprobado' if nota >= 7 else 'Reprobado'
    print(f"El nombre del estuidiante es {nombre}")
    print(f"lista del estudiante:{notas}")
    print(f"El promedio del estudiante es {promedio:.2f}")
    print(f"Estado: {estado}")
else:
    print("El estudiante no está registrado")



