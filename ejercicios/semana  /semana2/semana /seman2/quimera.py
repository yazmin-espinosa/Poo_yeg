class Quimera:
    def __init__(self, pelaje, color, tamano, fuerza, garras,
                  alas, no_cabezas, volar, cazar, altura):
        self.pelaje = pelaje
        self.color = color
        self.tamano = tamano
        self.fuerza = fuerza
        self.garras = garras
        self.alas = alas
        self.no_cabezas = no_cabezas
        self.volar = volar
        self.cazar = cazar
        self.altura = altura
        print(f"Pelaje {self.pelaje}")
        print(f"Color {self.color}")
        print(f"Tamaño {self.tamano}")
        print(f"Fuerza {self.fuerza}")
        print(f"Garras {self.garras}")
        print(f"Alas {self.alas}")
        print(f"Numero de cabezas {self.no_cabezas}")
        print(f"Vuela {self.volar}")
        print(f"Caza {self.cazar}")
        print(f"Altura {self.altura}")
descripcion = Quimera("Grueso", "Negro y Rojo", "4 m", "Capaz de destuir", 
                      "Afiladas", "Dragón", "4", "True", "true", "3 m")