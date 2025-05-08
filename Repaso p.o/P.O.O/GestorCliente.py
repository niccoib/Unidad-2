from ClaseCliente import Cliente
import csv
class ManejadorCliente:
    __ListaCliente: list

    def __init__(self):
        self.__ListaCliente = []

    def agregar_cliente(self, unCliente):
        self.__ListaCliente.append(unCliente)
    
    def cargar_cliente(self):
        archivo=open("/home/nico/Documentos/2do Año/P.O.O/ClientesAbril2024.csv" , encoding= 'utf-8')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader) 
        for fila in reader:
            cliente=Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]))
            self.agregar_cliente(cliente)
        archivo.close

    #Inciso A
    def actualizar_saldo(self, dni, mm):
        encontrado = False
        i= 0
        while i < len(self.__ListaCliente) and not encontrado:
            if self.__ListaCliente[i].get_dni() == dni:
                encontrado=True
                numerotarjeta= self.__ListaCliente[i].get_numTarjeta()
                saldoant= self.__ListaCliente[i].get_saldoAnterior()
                saldoact= mm.SaldoTotalMovimiento(numerotarjeta,saldoant)
            else: 
                i+=1
        
        if encontrado == True:
            print("Lista de Movimientos:")
            AyN= self.__ListaCliente[i].get_apellido() + '' + self.__ListaCliente[i].get_nombre()
            print("Cliente: {}".format(AyN))
            print("Numero de la Tarjeta: {}".format(self.__ListaCliente[i].get_numTarjeta))
            print("Saldo Anterior: {}".format(self.__ListaCliente[i].get_saldoAnterior()))
            mm.MostrarListado(numerotarjeta)
            print("Saldo Actual: {}".format(saldoact))

    
    #Inciso B
    def MostrarSiTuvoMovimientos(self,num,mm):
        encontrado= False
        i= 0
        while i< len(self.__ListaCliente) and not encontrado:
            if self.__ListaCliente[i].get_numTarjeta() == num:
                encontrado=True
                cantmov=mm.ContarMov(num)
                AyN= self.__ListaCliente[i].get_apellido() + '' + self.__ListaCliente[i].get_nombre()
            else:
                i+=1
        if encontrado == True:

            if cantmov > 0 :
                print("La persona {} tuvo movimientos en abril".format(AyN))
            else:
                print("La persona {} no tuvo movimientos en abril".format(AyN))
        else:
            print("No se encontro el Numero de Tarjeta asociado")
