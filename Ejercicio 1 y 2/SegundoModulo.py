from PrimerModulo import TarjetaSube
from CuartoModulo import ContenedorSubes
def Test():
    lista = ContenedorSubes()

    for i in range(2):
        saldo = float(input("Ingrese saldo de la tarjeta SUBE: "))
        numero = int(input("Ingrese numero de la tarjeta SUBE: "))

        tarjeta = TarjetaSube(saldo, numero)  # creación de instancia
        # print(tarjeta)  # se muestra la instancia
        lista.agregar_tarjetas(tarjeta)  # inciso 1

    lista.mostrar()  # inciso 2
    lista.mostrar_tarjetas()  # inciso 2

    nro = int(input("Ingrese numero de la tarjeta SUBE a buscar: "))
    lista.buscar_tarjeta(nro)  # inciso 3
        