# Lista para guardar los libros
# Cada libro es una lista con: [titulo, autor, genero, copias_totales, copias_disponibles]
libros = []

def agregar_libro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    copias = int(input("Numero de copias: "))

    encontrado = False
    for libro in libros:
        if libro[0] == titulo and libro[1] == autor:
            libro[3] = libro[3] + copias
            libro[4] = libro[4] + copias
            print("Se agregaron", copias, "copia(s) mas de:", titulo)
            encontrado = True
            break

    if encontrado == False:
        libros.append([titulo, autor, genero, copias, copias])
        print("Libro agregado:", titulo)

def buscar_libro():
    titulo = input("Titulo a buscar (deja vacio para ignorar): ")
    autor = input("Autor a buscar (deja vacio para ignorar): ")
    genero = input("Genero a buscar (deja vacio para ignorar): ")

    resultados = []
