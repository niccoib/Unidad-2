class Beneficiario:
    __dni:int
    __nombre: str
    __apellido: str
    __carreraencurso: str
    __siglaFacu: str
    __anio: int
    __promedio: int
    __idBeca: int   
    def __init__(self,dni,nombre,apellido,carreraencurso,siglaFacu,anio,promedio,idBeca):       
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__carreraencurso=carreraencurso
        self.__siglaFacu=siglaFacu
        self.__anio=anio
        self.__promedio=promedio
        self.__idBeca=idBeca
        
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_carreraencurso(self):
        return self.__carreraencurso
    def get_siglaFacu(self):
        return self.__siglaFacu
    def get_anio(self):
        return self.__anio
    def get_promedio(self):
        return self.__promedio
    def get_idBeca(self):
        return self.__idBeca
    
    def __gt__(self, otro):
        return self.get_siglaFacu() > otro.get_siglaFacu()
    def __str__(self):
        return "DNI: {} Nombre: {} Apellido: {} Carrera en curso: {} Sigla Facultad: {} Año: {} Promedio: {} ID Beca: {}".format(self.__dni,self.__nombre,self.__apellido,self.__carreraencurso,self.__siglaFacu,self.__anio,self.__promedio,self.__idBeca)