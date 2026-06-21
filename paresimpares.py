class ParesImares:
    def ExtraerPares(self,lista):
        nuevalista=[]
        for elemento in lista:
            if (elemento%2==0):
                nuevalista.append(elemento**2)
        return nuevalista

    def ExtraerImpares(self,lista:list)->list:
        nuevalista=[]
        for elemento in lista:
            if (elemento%2 ==1):
                nuevalista.append(elemento**3)
        return nuevalista
    
    #Impares -> cubo
    #pares -> cuadrado
def par(n:int)->bool:
    if n%2==0:
        return True
    else:
        return False
  

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
    obj=ParesImares()
    print(obj.ExtraerPares(lista))
    print(obj.ExtraerImpares(lista))

    print(par(169))
    VerifPar= lambda n: n%2 ==0 
    positivo= lambda n: n>0
    negativo= lambda n: n<0

    Mayor= lambda a,b:  a>b 
    print(f"Es par? {positivo(120)}")
    print(f"el valor es mayor {Mayor(120, 100)}")

    otraLista=list(map(lambda n:n**2,list(filter(lambda n:n%2==0,lista))))
    print(otraLista)

    edades=[8,23,14,16,31,25,28,11,44,52]
    MiNuevaLista= list(map (lambda edad : "eres mayor de edad" if (edad>=18) else"eres menor de edad",edades))
    print(edades)
    print(MiNuevaLista)
    listamitades=list(map(lambda n: n/2, list(filter(lambda n: n%2==0, edades))))
    print(listamitades)
