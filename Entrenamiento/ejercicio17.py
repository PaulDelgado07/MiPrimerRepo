import numpy as np
print("lista. -")
productos = ["Leche", "Pan", "Arroz", "Huevos", "Jugo"]
precios = [1.20, 0.85, 2.50, 1.75, 1.00] 

print("Mostrar la lista con sus porductos. -")
for i, (produc,p) in enumerate(zip(productos,precios), start=1):
    print(f"{i}. {produc}: precios: ${p}")

"""
El precio total

El producto más caro

El producto más barato
"""
print("\n")
precio_total = np.sum(precios)
print(f"El precio total:{precio_total:.2f}") 

Producto_caro = np.max(precios)
print(f"El producto más caro es: {Producto_caro}")

producto_barato = np.min(precios)
print(f"El producto mas barato: {producto_barato}")


