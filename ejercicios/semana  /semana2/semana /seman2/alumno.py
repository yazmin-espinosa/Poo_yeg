class Alumno:

    def __init__(self, nombre, matricula, carrera, promedio, cuatrimestre, 
                 correo_electronico, telefono, direccion, estatus, edad):
        
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.promedio = promedio
        self.cuatrimestre = cuatrimestre
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.direccion = direccion
        self.estatus = estatus
        self.edad = edad
        print(f"Nombre {self.nombre}")
        print(f"Matricula {self.matricula}")
        print(f"carrera {self.carrera}")
        print(f"Promedio {self.promedio}")
        print(f"Cuatrimestre {self.cuatrimestre}")
        print(f"Correo Electronico {self.correo_electronico}")
        print(f"Telefono {self.telefono}")
        print(f"Direccion {self.direccion}")
        print(f"Estatus {self.estatus}")
        print(f"Edad {self.edad}")

    def estudiar(self):
        print(f"Estudia {self.carrera}")

    def calcularPromedio(self):
        print(f"Promedio final{self.promedio}")

    def reinscribirse(self):
        print(f"Se reinscribio al {self.cuatrimestre}")

    def actualizarCorreo(self):
        print(f"{self.correo_electronico} actualizado")

    def actualizarTelefono(self):
        print(f"{self.telefono} actualizado")

antonio = Alumno("Antonio", "2120081291", "TIC´S", "9.5", "3", "2120081291@utectulancingo.edu.mx", 
                     "552346790", "Tulancingo", "Activo", "20")

antonio.estudiar()
antonio.calcularPromedio()
antonio.reinscribirse()
antonio.actualizarCorreo()
antonio.actualizarTelefono()