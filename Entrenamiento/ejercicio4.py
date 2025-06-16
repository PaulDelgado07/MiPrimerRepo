"""
🧠 Ejercicio: Contador de vocales en una frase
Enunciado:
1.Crea un programa en Python que:
2.Pida al usuario ingresar una frase o texto.
3.Cuente cuántas veces aparece cada vocal (a, e, i, o, u).
4.Ignore mayúsculas y tildes.
Imprima cuántas veces aparece cada vocal."""

print("Contador de palabras")

text = input("Ingrese un frase o un texto: ").lower()

text = text.replace("á","a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

contador_vocal_a = 0 
contador_vocal_e = 0 
contador_vocal_i = 0 
contador_vocal_o = 0 
contador_vocal_u = 0 

for i in text: 
    if i == "a":
        contador_vocal_a += 1
    elif i == "e":
        contador_vocal_e += 1
    elif i == "i":
        contador_vocal_i += 1
    elif i == "o":
        contador_vocal_o += 1
    elif i == "u": 
        contador_vocal_u += 1

print(f"palabras 'a': {contador_vocal_a} ")
print(f"palabras 'e': {contador_vocal_e} ")
print(f"palabras 'i': {contador_vocal_i} ")
print(f"palabras 'o': {contador_vocal_o} ")
print(f"palabras 'u': {contador_vocal_u} ")