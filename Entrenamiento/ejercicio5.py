"""🧠 Ejercicio: Verificar si un número es primo
Enunciado:

Haz un programa en Python que:

Pida al usuario que ingrese un número entero mayor que 1.

Verifique si ese número es primo.

Imprima si es primo o no.

Un número primo solo se puede dividir entre 1 y él mismo (por ejemplo: 2, 3, 5, 7, 11...)."""
numero = int(input("Ingresa un número entero mayor que 1: "))

if numero <= 1:
    print("El número debe ser mayor que 1.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")