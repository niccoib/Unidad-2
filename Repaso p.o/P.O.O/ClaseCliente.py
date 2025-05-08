class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numTarjeta: int
    __saldoAnterior: int

    def __init__(self,nom,ap,dni,numT,saldo):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__numTarjeta = numT
        self.__saldoAnterior = saldo
    
    def __str__(self):
        return "NOMBRE: {}, APELLIDO: {}, DNI: {}, NUMERO DE TARJETA: {}, SALDO ANTERIOR: {}".format(self.__nombre, self.__apellido, self.__dni ,self.__numTarjeta, self.__saldoAnterior)
    
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_dni(self):
        return self.__dni
    def get_numTarjeta(self):
        return self.__numTarjeta
    def get_saldoAnterior(self):
        return self.__saldoAnterior
    