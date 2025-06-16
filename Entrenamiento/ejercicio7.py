import math 
print("Raiz cuadrada")

numero = 16
raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz}")

print("_________________________________")

print("Potencias")
base = 2 
exponente = 5 

resultado = math.pow(base, exponente)

print(f"el resultado es:{resultado}")
print("________________________________")

print("redondeo hacia abajo")

x = 7.8 
print(f"Este es el redondeo de:", math.floor(x))

print("________________________________")

print("Redondeo hacia arriba ")
x = 7.2 
print(f"Este es el redondeo:", math.ceil(x))

print("________________________________")

print("Valor absoluto") 

resultado = (-5 - 2)
print(resultado)
print(f"Este es el resultado", math.fabs(resultado))

print("________________________________")

n = 5 
print(f"Resultado del factorial:", math.factorial(n))
print("_________________________________")
x = 1000 
print("resultado de algoritmo: ", math.log10(x))

print("__________________________________________")

x = 6 
print(f"Este es el resultado exponencial:", math.pow(float(x),2))

