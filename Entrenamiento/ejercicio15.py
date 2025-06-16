import numpy as np 

precios = np.array([12.5, 8.99, 15.0, 5.75, 22.30])

print("Mostrar lista de prodcutos: ")
for i, precio  in enumerate(precios, start = 1): 
    print(f"Productos {i}: {precio}")

totat_productos = np.sum(precios)
promedio_productos = np.mean(precios)

print(f"Precio total: {totat_productos:.2f}")
print(f"Promedio total de productos: {promedio_productos:.2f}")

