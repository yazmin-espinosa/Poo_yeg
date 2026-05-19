class Perro:
    def __init__(self,raza, tamano, peso, color, temperamento,
                 cola, edad, osico, orejas, pelaje):
        self.raza = raza
        self.tamano = tamano
        self.peso = peso
        self.color = color
        self.temperamento = temperamento
        self.cola = cola
        self.edad = edad
        self.osico = osico
        self.orejas = orejas
        self.pelaje = pelaje
        print(f"Raza {self.raza}")
        print(f"Tamaño {self.tamano}")
        print(f"Peso {self.peso}")
        print(f"Color {self.color}")
        print(f"Temperamento {self.temperamento}")
        print(f"Cola {self.cola}")
        print(f"Edad {self.edad}")
        print(f"Osico {self.osico}")
        print(f"Orejas {self.orejas}")
        print(f"Pelaje {self.pelaje}")
descripcion = Perro("Husky", "60 cm", "27 kg", "Café", "Amigable", "40 cm", 
                    "15 años", "15 cm", "12 cm Triangulares", "Esponjoso",) 