from ManejadorBecas import ManejadorBecas
from ManejadorBeneficiarios import ManejadorBeneficiario
def menu():
    print("Menu de Opciones")
    print("1- Cargar Beneficiarios")
    print("2- Cargar Becas")
    print("3-Mostrar los Beneficiarios de una beca y el importe total que debe disponer la Secretaria para el pago de dicha beca")
    print("4-Informar si un Beneficiario tiene mas de una beca")
    print("5-Listar Beneficiarios de mayor a menor por Facultad")
    print("6-Listar Beneficiarios que poseen promedio mayor a 8, que no poseen una beca")
if __name__ == "__main__":
    mbecas = ManejadorBecas()
    mbene = ManejadorBeneficiario()
    opcion= -1
    while opcion != 0:
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            mbene.cargar_beneficiarios()
            print("Datos de los Beneficiarios cargados correctamente.")
        elif opcion == 2:
            mbecas.cargar_becas()
            print("Datos de las Becas cargados correctamente.") 
        elif opcion == 3:
            tipo=input("Ingrese el tipo de beca:")
            idBuscar= mbecas.BuscarBeca(tipo)
            if idBuscar == -1:
                print("No se encontró la beca")
            else:
                cont=mbene.mostrarYcontar(idBuscar)
                importetotal= mbecas.get_importetotal(idBuscar,cont)
                print("El import e total que debe disponer la Secretaria para el pago de dicha beca es: {}".format(importetotal))
            
        
        elif opcion == 4:
            xdni=int(input("Ingrese DNI: "))
            mbene.MostrarCantBecas(xdni)
        elif opcion == 5:
            mbene.ListarBeneficiariosMayorMenor()
        elif opcion == 6:
            mbene.ListarPromMayor8()
        elif opcion == 0:
            print("Saliendo del programa...")
        
        else:
            print("Opción inválida. Intente nuevamente.")