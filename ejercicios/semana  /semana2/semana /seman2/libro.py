class Libro:

    def __init__(self, titulo, autor, genero, editorial, codigo, estado,
                 no_paginas, idioma, fecha_prestamo, fecha_devolucion):
        
        self.titulo = titulo 
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.codigo = codigo
        self.estado = estado
        self.no_paginas = no_paginas
        self.idioma = idioma
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        print(f"Titulo {self.titulo}")
        print(f"Autor {self.autor}")
        print(f"Genero {self.genero}")
        print(f"Editorial {self.editorial}")
        print(f"Codigo {self.codigo}")
        print(f"Estado {self.estado}")
        print(f"Numero de paginas {self.no_paginas}")
        print(f"Idioma {self.idioma}")
        print(f"Fecha de prestamo {self.fecha_prestamo}")
        print(f"Fecha de devolucion {self.fecha_devolucion}")

    def nombre(self):
        print(f"{self.titulo}")

    def prestamo(self):
        print(f"{self.fecha_prestamo}")
        
    def devolucion(self):
        print(f"{self.fecha_devolucion}")

    def generoPertenece(self):
        print(f"{self.genero}")
    
    def estadoLibro(self):
        print(f"{self.estado}")

it = Libro("IT", "Stephen King", "Teror", "Viking Press", "LIBTERROR001", 
         "Buen estado", "1138", "Español", "09/01/2026", "25/05/2026")

it.nombre()
it.prestamo()
it.devolucion()
it.generoPertenece()
it.estadoLibro()