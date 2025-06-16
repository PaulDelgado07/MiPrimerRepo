"""🎯 Ejercicio: Clase Producto para manejar inventario
✅ Objetivo:
Crear una clase Producto con:

Nombre del producto

Precio unitario

Cantidad en stock

Tener métodos para:

Mostrar información

Calcular el valor total en inventario

Aplicar un descuento al precio"""

class producto: 
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad 

    def mostrar_informacion(self): 
        print(f"Prodcuto: {self.nombre}")
        print(f"precio unitario: {self.precio:.2f}")
        print(f"Cantidad en stock: {self.cantidad:.2f}")

    def Calcular_valor_total(self):
        return self.precio * self.cantidad 

    def  aplicar_descuento(self, porcentaje):
        descuento = self.precio *(porcentaje/100)
        self.precio -= descuento

p1 = producto("laptop", 1200 , 5)

p1.mostrar_informacion()
print(f"Valor total del en inevntario: {p1.Calcular_valor_total}")