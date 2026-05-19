class Banco:
    def __init__(self, no_clientes, no_elementos_seguridad, no_edificios,
                 sistema_informatico, nombre_banco, no_cajeros,
                 fiable, capital, horario_atencion, color_banco):
        self.no_clientes = no_clientes
        self.no_elementos_seguridad = no_elementos_seguridad
        self.no_edificios = no_edificios
        self.sistema_informatico = sistema_informatico
        self.nombre_banco = nombre_banco
        self.no_cajeros = no_cajeros
        self.fiable = fiable
        self.capital = capital
        self.horario_atencion = horario_atencion
        self.color_banco = color_banco
        print(f"Numero de clientes {self.no_clientes}")
        print(f"Numero de elementos de seguridad {self.no_elementos_seguridad}")
        print(f"Numero de edificios {self.no_edificios}")
        print(f"Sistema informatico {self.sistema_informatico}")
        print(f"Nombre del banco {self.nombre_banco}")
        print(f"Numero de cajeros {self.no_cajeros}")
        print(f"Es fiable {self.fiable}")
        print(f"Capital {self.capital}")
        print(f"Horario de atencion {self.horario_atencion}")
        print(f"Color del banco {self.color_banco}")
acme = Banco(100000000, "3 Guardias", "2 Pisos", "Core Banking", "SANTANDER",
             "10 Cajeros", True, 50000000, "8:00 am a 4:00 pm", "Rojo y Blanco")