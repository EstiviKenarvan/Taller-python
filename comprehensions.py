def MiRango(n:int):
    for i in range(n):
        if(i<5):
            yield i
        else:
            return i
        
if __name__ == "__main__":
    res:int
    Milista=[]
    for i in MiRango(10):
        Milista.append(i**2)

    
      #"Mayor de edad" if edad >=18 else "Menor de edad"
      # i**2 for i in range(10)
    cuadrados=[i**2 for i in range(10)]

    print(Milista)
    print(cuadrados)