from PrimerModulo import TarjetaSube
class ContenedorSubes:
    __tarjetas:list
    
    def __init__(self):
        self.__tarjetas=[]
        
    def agregar_tarjetas(self,Tarjeta_Sube): #inciso 1
        self.__tarjetas.append(Tarjeta_Sube)
        
    def mostrar(self):
        for tarjeta in self.__tarjetas:
            print(tarjeta)
            
    def mostrar_tarjetas(self): #inciso 2
        for tarjeta in self.__tarjetas:
            if tarjeta.consultarSaldo() < 0 :
                print(tarjeta.getNumero())
    
    def buscar_tarjeta(self,nro): #inciso 3
        i=0
        encontrada=False
        while i < len(self.__tarjetas) and not encontrada:
            if self.__tarjetas[i].getNumero() == nro:
                print(f"Saldo de la tarjeta '{self.__tarjetas[i].consultar_saldo()}'")
                encontrada=True
            else:
                i+=1
        if not encontrada:
            print("La tarjeta no ha sido encontrada")
       