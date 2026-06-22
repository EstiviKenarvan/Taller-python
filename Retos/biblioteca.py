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

    for libro in libros:
        coincide_titulo = titulo == "" or titulo.lower() in libro["titulo"].lower()
        coincide_autor = autor == "" or autor.lower() in libro["autor"].lower()
        coincide_genero = genero == "" or genero.lower() in libro["genero"].lower()

        if coincide_titulo and coincide_autor and coincide_genero:
            resultados.append(libro)

    return resultados


def prestar_libro(titulo):
    # Busca el libro por titulo y, si hay copias disponibles, lo presta
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["copias_disponibles"] > 0:
                libro["copias_disponibles"] -= 1
                print("Prestamo exitoso:", libro["titulo"])
                print("Copias disponibles ahora:", libro["copias_disponibles"])
            else:
                print("No hay copias disponibles de:", libro["titulo"])
            return

    print("El libro no se encontro:", titulo)


def devolver_libro(titulo):
    # Busca el libro por titulo y, si estaba prestado, lo devuelve
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["copias_disponibles"] < libro["copias_totales"]:
                libro["copias_disponibles"] += 1
                print("Devolucion exitosa:", libro["titulo"])
                print("Copias disponibles ahora:", libro["copias_disponibles"])
            else:
                print("Todas las copias ya estaban en la biblioteca:", libro["titulo"])
            return

    print("El libro no se encontro:", titulo)


def mostrar_disponibles():
    # Muestra todos los libros que tienen al menos una copia disponible
    hay_disponibles = False

    for libro in libros:
        if libro["copias_disponibles"] > 0:
            hay_disponibles = True
            print("Titulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Genero:", libro["genero"])
            print("Disponibles:", libro["copias_disponibles"], "/", libro["copias_totales"])
            print("---")

    if not hay_disponibles:
        print("No hay libros disponibles en este momento.")


def mostrar_menu():
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            mostrar_disponibles()
        elif opcion == "6":
            print("Hasta luego!")
            break 
        else:
            print("Opcion invalida. Elige un numero del 1 al 6.")