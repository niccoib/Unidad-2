import csv
from departamento import Depto
class manejadorD:
    __deptos:list
    
    def __init__(self):
        self.__deptos=[]
    
    def agregarD(self,depto):
        self.__deptos.append(depto)
    
    def cargarDeptos(self):
        archivo=open("Departamentos.csv")
        reader= csv.reader(archivo,delimiter = ';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                unDepa= Depto(int(fila[0]),fila[1])
                self.__listaDepartamento.append(unDepa)
        archivo.close()