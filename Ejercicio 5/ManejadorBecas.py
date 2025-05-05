import csv
from Beca import Beca
class ManejadorBecas:
    __ListaBecas:list
    
    def __init__(self):
        self.__ListaBecas=[]
    def agregar_beca(self,unaBeca):
        self.__ListaBecas.append(unaBeca)
    def cargar_becas(self):
        saltear= False
        with open("c:/Codigos Facu/2do Año/Ejercicio 5/becas.csv") as archivoBecas:
            reader= csv.reader(archivoBecas,delimiter = ';')
            bandera= True
            for Bec in reader:
                if not saltear:
                    saltear=True
                else:
                    unaBeca=Beca(int(Bec[0]),Bec[1],float(Bec[2]))
                    self.agregar_beca(unaBeca)
        archivoBecas.close()
    def get_importetotal(self,idBuscar,cont):
        i=0
        encontrado=False
        importetotal=-1
        while i < len(self.__ListaBecas) and not encontrado:
            if self.__ListaBecas[i].get_idBeca() == idBuscar:
                encontrado=True
                importetotal=self.__ListaBecas[i].get_importeBeca()*cont
            else:
                i+=1
        return importetotal
    def BuscarBeca(self,tipo):
        encontrado=False
        i=0
        id=-1
        while i < len(self.__ListaBecas) and not encontrado:
            if self.__ListaBecas[i].get_tipoBeca() == tipo:
                encontrado=True
                id=self.__ListaBecas[i].get_idBeca()
            else:
                i+=1
        return id