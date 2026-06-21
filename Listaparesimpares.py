class ParesImpares:
    def ExtraePares (self, lista):
        nuevalista=[]
        for elemento in lista:
            if (elemento%2 ==0):
                nuevalista.append(elemento)
        return nuevalista
    
    def ExtraeImpares (self,lista:list)-> list:
        nuevalista=[]
        for elemento in lista:
            if (elemento%2 ==1):
                nuevalista.append(elemento)
        return nuevalista
    
    def imparescubos(self, lista:list)-> list:
        nuevalista=[]
        for elemento in lista:
            if (elemento%2 ==1):
                nuevalista.append(elemento**3)
        return nuevalista
    
    def parescuadrados(self, lista:list)-> list:
        nuevalista=[]
        for elemento in lista:
            if (elemento%2 ==0):
                nuevalista.append(elemento**2)
        return nuevalista
    
    def Par(n:int)-> bool:
        if (n%2 ==0):
            return True
        else:
            return False
    

if __name__ == '__main__':
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    obj=ParesImpares()
    print(obj.ExtraePares(lista))
    print(obj.ExtraeImpares(lista))
    print(obj.parescuadrados(lista))
    print(obj.imparescubos(lista))

    VerifPar=lambda n: n%2==0
    print(VerifPar(4))

    positivo=lambda n: n>0
    negativo=lambda n: n<0

    Mayordedos=lambda a,b: a>b

    print(f"el numero es positivo?: {positivo(-9)}")
    print(f"el numero es negativo?: {negativo(-9)}")
    print(f"el valor a es mayor que el valor b?: {Mayordedos(10, 5)}")

    NuevaLista=list(filter(lambda n: n%2==0, lista))
    print(NuevaLista)

    OtraLista=list(map(lambda n: n**2, filter(lambda n: n%2==0, lista)))
    print(OtraLista) 