import numpy as np

# Paso 1: Lista de temperaturas en grados Celsius
celsius = np.array([25, 30, 15, 10, 35])

fahrenheit = celsius*(9/5)+32
print("Mostrar las dos listas lado y lado. - ")

for i,(c,f) in enumerate(zip(celsius, fahrenheit), start=1):
    print(f"Día {i}: {c}°C -> {f:.2f}°F")

print("\nPromedios de grados Celcius y Fahrenheit. - ")
promedio_celsius = np.mean(celsius)
print(f"Promedio Celsius:{promedio_celsius}C")

promedio_fahrenheit = np.mean(fahrenheit)
print(f"Promedio fahrenheit:{promedio_fahrenheit}°F")

