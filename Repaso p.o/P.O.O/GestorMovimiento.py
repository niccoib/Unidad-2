from ClaseMovimiento import Movimiento
import numpy as np
import csv

class ManejadorMovimiento:
    __ListaMovimientos: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=21, incremento=1):
        self.__dimension= dim
        self.__incremento= incremento
        self.__cantidad=0
        self.__ListaMovimientos= np.empty(self.__dimension, dtype= Movimiento)
    
    def agregar_movimiento(self, unMovimiento):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__ListaMovimientos.resize(self.__dimension)
        self.__ListaMovimientos[self.__cantidad] = unMovimiento
        self.__cantidad+=1

    def cargar_movimiento(self):
        archivo= open("/home/nico/Documentos/2do Año/P.O.O/MovimientosAbril2024.csv", encoding='utf-8')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            movimiento= Movimiento(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
            self.agregar_movimiento(movimiento)
        archivo.close

     #Inciso A   
    def SaldoTotalMovimiento(self, num, saldo):
        for i in range(self.__cantidad):
            if self.__ListaMovimientos[i].get_NumTarjeta() == num:
                if self.__ListaMovimientos[i].get_TipoMov() == 'c':
                    saldo+= self.__ListaMovimientos[i].get_Importe()

                elif self.__ListaMovimientos[i].get_TipoMov() == 'p':
                    saldo= self.__ListaMovimientos[i].get_Importe()
        return saldo
    
    def MostrarListado(self, num):
        print("Movimientos")
        for i in range(self.__cantidad):
            if self.__ListaMovimientos[i].get_NumTarjeta() == num:
                print(self.__ListaMovimientos[i])
    
    #Inciso B
    def ContarMov(self,num):
        cont=0
        for i in range(self.__cantidad):
            if self.__ListaMovimientos[i].get_NumTarjeta() == num:
                fecha= self.__ListaMovimientos[i].get_fecha()
                mes= int(fecha.split("/")[1])
                if mes == 4:
                    cont+=1
        return cont
    
    #Inciso C
    def OrdenarPorNumero(self):
        self.__ListaMovimientos.sort()
        print("Listado Ordenado")