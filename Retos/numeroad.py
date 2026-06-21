import random

numero = random.randint(1, 100)

def adivina_el_numero(numero):
    contador = 0
    while True:
        entrada = input("Adivina el número entre 1 y 100: ")
        prediccion = int(entrada)
        contador += 1

        if prediccion == numero:
            print(f"Felicidades Has adivinado el número {numero} en {contador} intentos")
            break
        elif prediccion < numero:
            print(f"intento numero {contador}")
            print("Demasiado bajo, prueba con un número más alto")
        else:
            print(f"intento numero {contador}")
            print("Demasiado alto, prueba con un número más bajo")

        if contador == 10:
            print("no brother, alcanzaste el límite de intentos. El número era:", numero)
            break

adivina_el_numero(numero)