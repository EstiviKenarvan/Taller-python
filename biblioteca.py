# Lista global donde se guardan todos los libros
# Cada libro es un diccionario con: titulo, autor, genero, copias_totales, copias_disponibles
libros = []


def agregar_libro(titulo, autor, genero, copias):
    # Buscar si el libro ya existe (mismo título y autor)
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["autor"].lower() == autor.lower():
            # Si ya existe, solo se suman las copias
            libro["copias_totales"] += copias
            libro["copias_disponibles"] += copias
            print("Se agregaron", copias, "copia(s) mas de:", titulo)
            return

    # Si no existe, se crea un diccionario nuevo y se agrega a la lista
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "copias_totales": copias,
        "copias_disponibles": copias
    }
    libros.append(nuevo_libro)
    print("Libro agregado:", titulo)


