from GestorCliente import ManejadorCliente
from GestorMovimiento import ManejadorMovimiento

def menu():
    print("Menu de Opciones")
    print("1) Actualizar Saldo y armar listado")
    print("2) Informar si el cliente no tuvo movimientos durante el mes de abril")
    print("3) Ordenar Movimientos")
    print("0) Para Finalizar")
if __name__ == "__main__":
    mc= ManejadorCliente()
    mm=ManejadorMovimiento()
    mc.cargar_cliente
    mm.cargar_movimiento

    opcion= -1
    while opcion != 0:
        menu()
        opcion= int(input('Seleccione una opcion: '))
        if opcion == 1:
            dni= int(input('Ingrese el DNI: '))
            mc.actualizar_saldo(dni,mm)

        elif opcion == 2:
            num=int(input('Ingrese Numero de Tarjeta')) 
            mc.MostrarSiTuvoMovimientos(num,mm)

        elif opcion == 3:
            mm.OrdenarPorNumero()