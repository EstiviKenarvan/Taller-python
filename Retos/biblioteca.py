# Lista para guardar los libros
libros = []

def agregar_libro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    copias = int(input("Numero de copias: "))

    encontrado = False
    for libro in libros:
        # Ahora usamos claves de diccionario
        if libro["titulo"].lower() == titulo.lower() and libro["autor"].lower() == autor.lower():
            libro["copias_totales"] += copias
            libro["copias_disponibles"] += copias
            print("Se agregaron", copias, "copia(s) mas de:", titulo)
            encontrado = True
            break

    if not encontrado:
        # Guardamos el libro como un diccionario en lugar de una lista
        libros.append({
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "copias_totales": copias,
            "copias_disponibles": copias
        })
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

    # Imprimimos los resultados 
    if resultados:
        print("\n--- Resultados de busqueda ---")
        for libro in resultados:
            print(f'- {libro["titulo"]} de {libro["autor"]} ({libro["copias_disponibles"]} disponibles)')
    else:
        print("\nNo se encontraron libros que coincidan.")

def prestar_libro(titulo):
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
            # Pedimos el título antes de llamar a la función
            titulo_prestar = input("Ingresa el titulo del libro a prestar: ")
            prestar_libro(titulo_prestar)
        elif opcion == "4":
            # Pedimos el título antes de llamar a la función
            titulo_devolver = input("Ingresa el titulo del libro a devolver: ")
            devolver_libro(titulo_devolver)
        elif opcion == "5":
            mostrar_disponibles()
        elif opcion == "6":
            print("Hasta luego!")
            break 
        else:
            print("Opcion invalida. Elige un numero del 1 al 6.")

if __name__ == "__main__":
    mostrar_menu()