import numpy as np
import csv
from Carrera import carrera 
class ManejadorC:
    __ArreC: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento = 1
    def __init__(self, dimension=10, incremento=1):
        self.__ArreC = np.empty(dimension, dtype=carrera)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        
    def agregarCarrera(self, unaCarrera):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__ArreC.resize(self.__dimension)
        self.__ArreC[self.__cantidad]=unaCarrera
        self.__cantidad += 1
        
    def cargar_carrera(self):
        saltear = False
        with open("c:/Codigos Facu/2do Año/Ejercicio 4/Carreras.csv", encoding="utf-8") as archivocarrera:
            reader = csv.reader(archivocarrera, delimiter=';')
            for carr in reader:
                if not saltear:
                    saltear = True
                else:
                    unacarr = carrera(int(carr[0]), carr[1], carr[2], carr[3], carr[4], int(carr[5]))
                    self.agregarCarrera(unacarr)
        archivocarrera.close()
                    
  
    def buscar_carrera(self,nombre):
        i=0
        aux = -1
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__ArreC[i].getNombre() == nombre:
                aux = int( self.__ArreC[i].getidFacultad() )
                encontrado= True
            else:
                i +=1
        return aux
    def cantidad(self,id):
        cont=0
        for i in range(self.__cantidad):
            if self.__ArreC[i].getidFacultad() == id:
                cont+=1
        return cont
    
    def listar_y_ordenar(self, id_facultad):
        carreras = []
        # Filtrar las carreras por el ID de la facultad
        for i in range(self.__cantidad):
            if self.__ArreC[i].getidFacultad() == id_facultad:
                carreras.append(self.__ArreC[i])
        
        # Ordenar las carreras alfabéticamente por nombre
        carreras.sort(key=lambda x: x.getNombre())
        
        # Imprimir las carreras ordenadas
        for carrera in carreras:
            print("Nombre: {}, Duración: {}".format(carrera.getNombre(), carrera.getDuracion()))
        
