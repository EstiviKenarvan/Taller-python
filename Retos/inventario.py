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
def vender_producto():
    nombre = input("Nombre del producto a vender: ")

    encontrado = False
    for producto in inventario:
        if producto[0] == nombre:
            inventario.remove(producto)
            print("Producto vendido y retirado del inventario.")
            encontrado = True
            break

    if encontrado == False:
        print("Producto no encontrado.")

# Programa principal
while True:
    print("\n--- Inventario Básico ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        vender_producto()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")