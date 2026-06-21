#esto es el main principal
if __name__ == "__main__":

    a:int
    b:int
    a=input("Ingrese el valor de a: ")
    b=input("Ingrese el valor de b: ")
    print (type(a))
    print (type(b))
    if a > b:
        print(f"a es mayor que {a}")
    else:
        print(f"b es mayor que {b}")
    print("gracias por ejecutarme")