"""
🧠 Tema: Clase Libro
🎯 Objetivo:
Crear una clase sencilla llamada Libro que tenga:

Título

Autor

Número de páginas

Y un método para:

Mostrar la información del libro

"""
class libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas 
    
    def mostrar_info(self): 
        print(f"Título:{self.titulo}")
        print(f"Autor {self.autor}")
        print(f"Números de paginas: {self.numero_paginas}")

libro1 = libro("Luis Gonzales", "Paul David", 103)

libro1.mostrar_info()