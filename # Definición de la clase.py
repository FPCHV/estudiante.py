# Definición de la clase

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    # Método para mostrar información
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)

    # Método para simular una acción
    def estudiar(self):
        print(self.nombre, "está estudiando", self.carrera)


# Creación de objetos

estudiante1 = Estudiante("Juan Pérez", 20, "Ingeniería en Sistemas")
estudiante2 = Estudiante("María López", 22, "Administración de Empresas")

# Uso de los métodos

print("=== Estudiante 1 ===")
estudiante1.mostrar_datos()
estudiante1.estudiar()

print("\n=== Estudiante 2 ===")
estudiante2.mostrar_datos()
estudiante2.estudiar()