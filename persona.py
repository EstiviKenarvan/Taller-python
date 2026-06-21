class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print("Hola, me llamo", self.nombre, "y tengo", self.edad, "años")
    def cumpleanos(self):
        self.edad += 1
        print("Feliz cumpleanos", self.nombre, "! Ahora tienes", self.edad, "años")
p1 = Persona("Axel", 20)
p1.saludar()
p1.cumpleanos()
