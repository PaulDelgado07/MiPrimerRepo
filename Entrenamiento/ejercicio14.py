import numpy as np 

np.random.seed()

calificaciones = np.random.uniform(0,10,(4,5))

print("Matriz de calificaciones(4 estudiantes y 5 materias)")

promedios_estudiantes = np.mean(calificaciones, axis= 1)
print("promedio por estudiante:")
for i, promedio in enumerate(promedios_estudiantes, start = 1):
    print(f"Estudiante {i}: {promedio:.2f}")


promedio_por_materia = np.mean(calificaciones, axis= 0)
print("Promedio de las calificaciones por materia: ")
for i, promedio in enumerate(promedio_por_materia, start = 1):
    print(f"Materia {i} : {promedio:.2f}")


mejor_promedio = np.argmax(promedios_estudiantes)
print(f"Este es el estudiante con mayor promedio: {mejor_promedio + 1}")


