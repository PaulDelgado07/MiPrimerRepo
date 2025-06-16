"""
Crea un programa que:

1. Cuente cuántos números son mayores que cero.
2. Cuente cuántos números son menores que cero.
3. Cuente cuántos números son iguales a cero.
Imprima los tres resultados.
"""

numeros = [3, -1, 0, 7, -4, 0, 6, -9, 2, 0]

numeros_mayores = 0 
numeros_menores = 0 
iguales_cero = 0 

for i in numeros: 
    if i > 0:
        numeros_mayores += 1
    elif i < 0: 
        numeros_menores +=1 
    else: 
        iguales_cero += 1 

print(f"Resultado de los nmumeros mayores: {numeros_mayores}")
print(f"Resultadi de los numeros menores: {numeros_menores}")
print(f"Resultado de los numeros iguales a cero: {iguales_cero}")