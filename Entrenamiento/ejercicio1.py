"""
Escribe un programa en Python que:
Recorra el arreglo.
Sume por separado:
Todos los números positivos (incluyendo el cero).
Todos los números negativos.
Imprima el resultado al final."""
"""
numeros = [5, -3, 7, -1, -6, 4, 0, -2]  

suma_positivos = 0 
suma_negativos = 0 

for i in numeros: 
    if i >= 0:
        suma_positivos += i
    else: 
        suma_negativos += i 

print(f"Suma de numeros positivos:{suma_positivos}")
print(f"Suma de numeros negativos:{suma_negativos}")
"""

"""
Escribe un programa en Python que:
Recorra el arreglo.
Sume por separado:
Todos los números positivos (incluyendo el cero).
Todos los números negativos.
Imprima el resultado al final."""


numeros = [5, -3, 7, -1, -6, 4, 0, -2] 

numeros_positvos = 0 
numeros_negativos = 0 

for i in numeros:
    if i >= 0:
        numeros_positvos +=i 
    else: 
        numeros_negativos +=i
        
print(f"Numeros postivos: {numeros_positvos}")
print(f"Numeros negativos: {numeros_negativos}")