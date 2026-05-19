class Carro:
    def __init__(self, marca, modelo, color, num_puertas, placa, ano,
                 precio, velocidad_maxima, combustible, num_pasajeros):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.num_puertas = num_puertas
        self.placa = placa
        self.ano = ano
        self.precio = precio
        self.velocidad_maxima = velocidad_maxima
        self.combustible = combustible
        self.num_pasajeros = num_pasajeros
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Color {self.color}")
        print(f"Numero de puertas {self.num_puertas}")
        print(f"Placa {self.placa}")
        print(f"Año {self.ano}")
        print(f"Precio {self.precio}")
        print(f"Velocidad Maxima {self.velocidad_maxima}")
        print(f"Tipo de combustible {self.combustible}")
        print(f"Numero de pasajeros {self.num_pasajeros}")
    def encender(self):
        print(f"{self.marca} {self.modelo} encendiendo")
    def apagar(self):
        print(f"{self.marca} {self.modelo} apagando")
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando")
    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando")
    def abrirPuertas(self):
        print(f"Las puertas del {self.marca} {self.modelo} se abrieron")
versa = Carro("Nissan", "Versa", "Rojo", "4 Puertas", "ABC-123-x", "2023", "320000 MXN", "200 KM/H",
            "Gasolina","5 Pasajeros")
versa.encender()
versa.apagar()
versa.acelerar()
versa.frenar()
versa.abrirPuertas()