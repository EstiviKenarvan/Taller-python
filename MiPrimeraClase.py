class Persona:

    def __init__(self):
        self.nombre="juan"
        self.apellidos="perez lopez"

    #def es para definir un metodo
    def MiMetodo(self):
        print(f'hola {self.nombre}')
        
if __name__ == "__main__":
    obj=Persona()
    print (obj.nombre)
    print (obj.apellidos)
    obj.MiMetodo()
