class Atencion:
    __dni: int
    __fecha: str
    __importe: float
    
    def __init__(self,dni,fecha,importe):
        self.__dni= dni
        self.__fecha=fecha
        self.__importe= importe
        
    def get_dni(self):
        return self.__dni
    def get_fecha(self):
        return self.__fecha
    def get_importe(self):
        return self.__importe
    
    def __str__(self):
        return "DNI: {}, FECHA: {}, IMPORTE: {}".format (self.__dni, self.__fecha, self.__importe)