"""V🎯 Ejercicio: Clase Estudiante con métodos
✅ Objetivo:
Crear una clase llamada Estudiante

Guardar nombre y una lista de notas

Tener métodos para:

Mostrar la información

Calcular y devolver el promedio

Saber si el estudiante está aprobado (promedio ≥ 7)"""

class estudiante: 
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Notas: {self.notas}")

    def calcular_promedio(self):
        return sum(self.notas)/len(self.notas)

    def esta_aprobado(self):
        promedio = self.calcular_promedio()
        return promedio >= 7 


e1 = estudiante("Paul Delgado", [9, 10, 8])
e2 = estudiante("Koraima Merchán", [9, 10, 7])

e1.mostrar_info()
print(f"Promedio:{e1.calcular_promedio():.2f}")
print(f"¿Aprobado?: {e1.esta_aprobado()} ")
print("_____________________")
e2.mostrar_info()
print(f"Promedio:{e2.calcular_promedio():.2f}")
print(f"¿Aprobado?: {e2.esta_aprobado()} ")