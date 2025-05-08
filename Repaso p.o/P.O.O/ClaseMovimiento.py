class Movimiento:
    __NumTarjeta: int
    __fecha: str
    __descripcion: str
    __TipoMov: str
    __Importe: int

    def __init__(self,num,fecha,desc,tipo,imp):
        self.__NumTarjeta = num
        self.__fecha = fecha
        self.__descripcion = desc
        self.__TipoMov = tipo
        self.__Importe = imp

    def __str__(self):
        return "NUMERO DE TARJETA: {}, FECHA: {}, DESCRIPCION: {}, TIPO DE MOVIMIENTO: {}, IMPORTE {}".format(self.__NumTarjeta, self.__fecha, self.__descripcion, self.__TipoMov, self.__Importe)
    def __lt(self,otro):
        return self.__NumTarjeta < otro.__NumTarjeta

    def get_NumTarjeta(self):
        return self.__NumTarjeta
    def get_fecha(self):
        return self.__fecha
    def get_descripcion(self):
        return self.__descripcion
    def get_TipoMov(self):
        return self.__TipoMov
    def get_Importe(self):
        return self.__Importe
    
