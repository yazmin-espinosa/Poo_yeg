class Mesa:
    def __init__(self, material, color, forma, altura, ancho,
                  largo, no_patas, peso, capacidad, tipo):
        self.material = material
        self.color = color
        self.forma = forma 
        self.altura = altura 
        self.ancho = ancho 
        self.largo = largo
        self.no_patas = no_patas
        self.peso = peso 
        self.capacidad = capacidad
        self.tipo = tipo
        print(f"Material {self.material}")
        print(f"Color{self.color}")
        print(f"Forma {self.forma}")
        print(f"Altura {self.altura}")
        print(f"Ancho {self.ancho}")
        print(f"Largo {self.largo}")
        print(f"Numero de patas {self.no_patas}")
        print(f"Peso {self.peso}")
        print(f"Capacidad {self.capacidad}")
        print(f"Tipo {self.tipo}")
    def personas(self):
        print(f"{self.capacidad} personas estan sentendas")
    def uso(self):
        print(f"{self.tipo}")
    def moverMesa(self):
        print(f"{self.tipo} se movio de lugar")
    def mantel(self):
        print(f"{self.tipo} tiene un mantel")
    def tienePlatos(self):
        print(f"{self.tipo} tiene platos")
comedor = Mesa("Madera", "Cafe", "Rectangular", "1.20 cm", "30 cm", "60 cm", 
                    "2", "2 kg", "4", "Comedor")
comedor.personas()
comedor.uso()
comedor.moverMesa()
comedor.mantel()
comedor.tienePlatos()