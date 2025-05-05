from datetime import date
class carrera():
    __codigo:int
    __nombre:str
    __titulo: str
    __duracion:int
    __nivel:str
    __codigoFacultad:int
    def __init__(self,cod,nomb,titulo,duracion,nivel,codFacultad):
        self.__codigo=cod
        self.__nombre=nomb
        self.__titulo=titulo
        self.__duracion=duracion
        self.__nivel=nivel
        self.__codigoFacultad=codFacultad
    def __lt__(self,otro):
        return self.__nombre < otro.getNombre()
    def getCod(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getTitulo(self):  
        return self.__titulo  
    def getDuracion(self):
        return self.__duracion
    def getNivel(self):
        return self.__nivel
    def getidFacultad(self):
        return self.__codigoFacultad
     