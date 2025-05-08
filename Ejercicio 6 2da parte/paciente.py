class Paciente:
    __dni: int
    __nombre: str
    __unidad: str
    
    def __init__(self,dni,nombre,unidad):
        self.__dni = dni
        self.__nombre= nombre
        self.__unidad=unidad
    
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_unidad(self):
        return self.__unidad
    
    def __str__(self):
        return "DNI: {}, NOMBRE: {}, UNIDAD: {}".format(self.__dni, self.__nombre, self.__unidad)
    
    def __lt__(self,otro):
        return (self.get_unidad(), self.get_nombre()) < (otro.get_unidad(), otro.get_nombre())
    
    