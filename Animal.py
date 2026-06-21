class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def hablar(self):
        print(self.nombre, "dice:", self.sonido)
perro = Animal("Firulais", "Guau")
gato = Animal("Mishi", "Miau")
perro.hablar()
gato.hablar()

