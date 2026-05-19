class Transporte:
    def __init__(self, marca, modelo, color, tipo_combustible, velocidad_maxima,
                 num_puertas, num_pasajeros, placa, ano, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.velocidad_maxima = velocidad_maxima
        self.num_puertas = num_puertas
        self.num_pasajeros = num_pasajeros
        self.placa = placa
        self.ano = ano
        self.precio = precio
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Color {self.color}")
        print(f"Tipo de combustible {self.tipo_combustible}")
        print(f"Velocidad Maxima {self.velocidad_maxima}")
        print(f"Numero de puertas {self.num_puertas}")
        print(f"Numero de pasajeros {self.num_pasajeros}")
        print(f"Placa {self.placa}")
        print(f"Año {self.ano}")
        print(f"Precio {self.precio}")
    def encender(self):
        print(f"{self.marca} {self.modelo} encendiendo")
    def apagar(self):
        print(f"{self.marca} {self.modelo} apagando")
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando")
    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando")
    def tocarClaxon(self):
        print(f"{self.marca} {self.modelo} toco el claxon")
corolla = Transporte("Toyota", "Corolla", "Blanco", "Gasolina", "180 Km/H", "3 Puertas", "18 Pasajeros", "HTR-245-A",
                      "2025","350000 MXN")
corolla.encender()
corolla.apagar()
corolla.acelerar()
corolla.frenar()
corolla.tocarClaxon()