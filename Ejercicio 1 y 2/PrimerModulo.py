class TarjetaSube:
    __saldo=int
    __numero=int
    def __init__(self,saldo,numero):
        self.__saldo=int(saldo)
        self.__numero=int(numero)
    def __str__(self):
        return f"Tarjeta SUBE '{self.__numero}' - Saldo: '{self.__saldo}'"
    def get_nro(self):
        return f'{self.__numero}'
    def cargar_saldo(self,importe):
        if importe > 0:
            self.__saldo+=float(importe)
        elif importe < 0:
            print("No se puede cargar saldo negativo")
    def pagar_pasaje(self,importe):
        if self.__saldo > importe:
            self.__saldo= int(self.__saldo - importe) 
        elif self.__saldo < importe:
            print("Saldo Insuficiente")
    def consultar_saldo(self):
        return f"SALDO: '{self.__saldo}'"
    
        
