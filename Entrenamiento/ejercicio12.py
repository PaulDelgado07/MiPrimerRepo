"""
}🧮 Ejercicio: Calculadora de áreas y perímetros de figuras geométricas
Crea un programa que:
Le pida al usuario elegir entre cuadrado, círculo o triángulo.
Dependiendo de la figura elegida, pida los datos necesarios (lado, radio, base y altura, etc).
Calcule y muestre el área y el perímetro usando la librería math cuando sea necesario (por ejemplo, usar math.pi, math.sqrt).
Si la opción ingresada no es válida, muestre un mensaje de error.
"""
import math
print("--Calculadora de áres y perímetros de figuras geométricas--")

figuras = input("Elija la figura que desea: [Cuadrado, Círculo, triángulo]: ")
figuras_minuscula = figuras.lower

if figuras == "cuadrado": 
    lado = float(input("Ingrese el lado del cuadrado: "))
    print(f"El Area del cuadrado es: {math.pow(lado,2)}cm^2")
    print(f"El perimetro del cuadrado es: ",4*lado)

elif figuras == "circulo": 
    pi= math.pi
    radio = float(input("Ingrese el radio del circulo: "))
    print(f"El Area del circulo es:{(math.pi*radio**2)}")
    print(f"El circunsferencia del circulo es:{2*pi*radio}")

elif figuras == "triangulo":
    a = float(input("Ingresa el lado 'a': "))
    b = float(input("Ingresa el lado 'b': "))
    c = float(input("Ingresa el lado 'c': "))

    s = ((a+b+c)/(2))
    print(f"El semiperimetro es: {s}")
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"El ara del triangulo es:{area:f2}")

