import numpy as np
import csv
from Facultad import facultad
class ManejadorF:
    __ArreF: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento = int
    
    def __init__(self, dimension=10, incremento=1):
        self.__ArreF = np.empty(dimension, dtype=facultad)
        self.__cantidad = 0
        self.__dimension = dimension
        
    def agregarFacultad(self, unaFacultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__ArreF.resize(self.__dimension)
        self.__ArreF[self.__cantidad]=unaFacultad
        self.__cantidad += 1
    
    def cargarFacultad(self):
        saltear= False
        with open("c:/Codigos Facu/2do Año/Ejercicio 4/Facultades.csv") as archivoFacultad:
            reader= csv.reader(archivoFacultad,delimiter = ';')
            bandera= True
            for Fac in reader:
                if not saltear:
                    saltear=True
                else:
                    unaFacultad=facultad(int(Fac[0]),Fac[1],Fac[2],Fac[3],Fac[4])
                    self.agregarFacultad(unaFacultad)
        archivoFacultad.close()
        
    def MostrarFac(self,gc):
        for i in range(self.__cantidad):
            print("En la {} hay: {} carreras".format(self.__ArreF[i].get_nombre(), gc.cantidad(self.__ArreF[i].get_id())))
    def BuscarFacultad(self,id):
        i=0
        aux="-1"
        encontrado=False
        while i < self.__cantidad and not encontrado:
            if self.__ArreF[i].get_id() == id:
                aux = self.__ArreF[i].get_nombre()
                encontrado= True
            else:
                i +=1
        return aux
    
    def BuscarFacNom(self,nom):
        i=0
        aux= -1
        encontrado= False
        while i < self.__cantidad and not encontrado:
            if self.__ArreF[i].get_nombre() == nom:
                aux= self.__ArreF[i].get_id()
                encontrado= True
            else:
                i +=1
        return aux
        
        
            