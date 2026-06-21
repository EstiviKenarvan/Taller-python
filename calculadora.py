# Clase con operaciones matematicas basicas
class Calculadora:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b

# Usamos la calculadora
calc = Calculadora()
print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(10, 4))
print("Multiplicacion:", calc.multiplicar(3, 7))

# Salida:
# Suma: 8
# Resta: 6
# Multiplicacion: 21
