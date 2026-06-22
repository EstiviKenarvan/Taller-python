# Lista para guardar los productos
inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    # Buscar si el producto ya existe
    encontrado = False
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] = producto[1] + cantidad
            print("Producto ya existente, se aumentó el stock.")
            encontrado = True
            break

    # Si no existe, agregarlo como nuevo
    if encontrado == False:
        inventario.append([nombre, cantidad])
        print("Producto agregado.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("\n--- Inventario ---")
        for producto in inventario:
            print("Producto:", producto[0], "| Cantidad:", producto[1])
        print("------------------")

