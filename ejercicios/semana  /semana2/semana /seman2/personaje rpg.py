class PersonajeRpg:
    def __init__(self, nombre, clase, velocidad, nivel, vida, dano_hecho,
                 arma, armadura, habilidad_especial, oro):
        self.nombre = nombre
        self.clase = clase
        self.velocidad = velocidad
        self.nivel = nivel
        self.vida = vida
        self.dano_hecho = dano_hecho
        self.arma = arma
        self.armadura = armadura
        self.habilidad_especial = habilidad_especial
        self.oro = oro
        print(f"Nombre {self.nombre}")
        print(f"Clase {self.clase}")
        print(f"Velocidad {self.velocidad}")
        print(f"Nivel {self.nivel}")
        print(f"Vida {self.vida}")
        print(f"Daño hecho {self.dano_hecho}")
        print(f"Arma {self.arma}")
        print(f"Armadura {self.armadura}")
        print(f"Habilidad especial {self.habilidad_especial}")
    def atacar(self):
        print(f"{self.nombre} esta atacando")
    def defender(self):
        print(f"{self.nombre} se defendiendo")
    def usarHabilidad(self):
        print(f"{self.nombre} uso {self.habilidad_especial}")
    def curarse(self):
        print(f"{self.nombre} se esta curando")
    def subirNivel(self):
        print(f"{self.nombre} subiste de nivel")
freya = PersonajeRpg("Freya", "Guerrero", "67%", "Subiste de nivel 25", "32%", "76%", "Espada Legendaria",
                      "Armadura de Acero", "Golpe de Fuego", "15000 Monedas de Oro")
freya.atacar()
freya.defender()
freya.usarHabilidad()
freya.curarse()
freya.subirNivel()