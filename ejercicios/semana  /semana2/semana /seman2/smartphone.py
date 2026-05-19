class SmartPhone:
    def __init__(self, marca, modelo, color, sistema_operativo,
                 memoria_ram, almacenamiento, camara,
                 bateria, tamano_pantalla, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.sistema_operativo = sistema_operativo
        self.memoria_ram = memoria_ram
        self.almacenamiento= almacenamiento
        self.camara = camara
        self.bateria = bateria
        self.tamano_pantalla= tamano_pantalla
        self.precio = precio
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Color {self.color}")
        print(f"Sistema operativo {self.sistema_operativo}")
        print(f"Memoria RAM {self.memoria_ram}")
        print(f"almacenamiento {self.almacenamiento}")
        print(f"Camara {self.camara}")
        print(f"Bateria {self.bateria}")
        print(f"Tamaño de la pantalla {self.tamano_pantalla}")
        print(f"Precio {self.precio}")
samsung = SmartPhone("SAMSUNG", "GALAXY S25", "Torna azul", "Android 14", "8 GB RAM", "236 GB", "50 MP", "3900 mAh",
                     "6.1 Pulgadas", "18000 MXN")