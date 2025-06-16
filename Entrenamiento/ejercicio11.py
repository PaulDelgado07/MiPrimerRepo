"""+
Crea un programa que:
Le pida al usuario cuántas personas desea registrar.
Para cada persona, pida su nombre y edad.
Clasifique a cada persona como:
Niño (0 a 12 años)
Adolescente (13 a 17 años)
Adulto (18 a 59 años)
Adulto mayor (60 en adelante)
Muestre la información al final (nombre, edad, y clasificación)."""

personas = {} 

cantidad = int(input("Ingrese cuantas personas desea ingresar: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre [{i+1}]: ")
    edad = int(input("Ingresa tu edad: "))

    personas[nombre] = edad

for nombre, edad in personas.items(): 
    if edad <= 12:
        clasificacion = 'niño'
    elif edad <= 17: 
        Clasificacion = 'Adolescente' 
    elif edad <= 59: 
        clasificacion = 'Adulto'
    else: 
        clasificacion = 'Adulto mayor'
    
print(f"El nombre de ususario es {nombre} tiene como edad: {edad} y su clasificación es: {clasificacion}")
