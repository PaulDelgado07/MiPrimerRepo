"""🧠 Ejercicio: Verificar si una palabra es palíndromo
Enunciado:

Crea un programa que:

Pida al usuario que ingrese una palabra o frase.

Ignore los espacios y mayúsculas.

Verifique si la palabra o frase es un palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a izquierda (por ejemplo: "anita lava la tina").

Muestre un mensaje indicando si lo es o no."""

frase = input("Ingrese una palabra o frase: ")

frase_limpia = frase.replace(" ", "").lower()

if frase_limpia == frase_limpia[::-1]:
    print("La palabra es un palíndromo")
else: 
    print("La frase no es un palíndromo")