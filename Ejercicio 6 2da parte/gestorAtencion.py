from atencion import Atencion
import numpy as np
import csv
class ManejadorAtencion:
    __listaAtencion: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__(self, dim=48, incremento= 1):
        self.__dimension = dim
        self.__incremento= incremento
        self.__cantidad= 0
        self.__listaAtencion= np.empty(self.__dimension, dtype=Atencion)
        
    def agregar_atencion(self, unaAtencion):
        if self.__cantidad == self.__dimension:
            self.dimension += self.__incremento
            self.__listaAtencion.resize(self.dimension)
            print("Espacio de Memoria Solicitado")
        self.__listaAtencion[self.__cantidad] = (unaAtencion)
        self.__cantidad += 1
    
    def cargar_atenciones(self):
        archivo= open("c:/Codigos Facu/2do Año/Ejercicio 6 2da parte/atenciones.csv", encoding='utf-8')
        reader= csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
                atencion=Atencion(int(fila[0]), fila[1], int(fila[2]))
                self.agregar_atencion(atencion)
                print("Atencion Cargada.")
        archivo.close()
        
    def inciso_A(self, fecha):
        cont = 0
        imptotal = 0
        for i in range(self.__cantidad):
            if self.__listaAtencion[i].get_fecha() == fecha:
                cont += 1
                imptotal += self.__listaAtencion[i].get_importe()

        if cont > 0:
            print("Las atenciones realizadas en el día {} fueron {}. Importe total a pagar: {}".format(fecha, cont, imptotal))
        else:
            print("No se registraron atenciones en el día {}".format(fecha))

            
    def contar_atenciones(self, dni):
        cont= 0
        for i in range (self.__cantidad):
            if self.__listaAtencion[i].get_dni() == dni:
                cont += 1
        return cont