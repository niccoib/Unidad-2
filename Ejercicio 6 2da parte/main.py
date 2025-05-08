from gestorAtencion import ManejadorAtencion
from gestorPaciente import ManejadorPaciente

def menu():
    print("----- Menú de Opciones -----")
    print("1) Informar atenciones realizadas y el importe total a pagar dada una fecha")
    print("2) Informar el Nombre, Apellido y cantidad de atenciones que tuvo una persona dado su DNI")
    print("3) Listar los pacientes que no han tenido atenciones")
    print("4) Listar los pacientes ordenados por Apellido de menor a mayor")
    print("0) Salir")

if __name__ == "__main__":
    maten = ManejadorAtencion()
    mpaci = ManejadorPaciente()
    maten.cargar_atenciones()
    mpaci.cargar_pacientes()

    opcion = -1
    while opcion != 0:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            opcion = -1
            continue
        
        if opcion == 1:
            fecha = input("Ingrese fecha (formato dd/mm/aaaa): ")
            print(">> Ejecutando inciso A...")
            maten.inciso_A(fecha)
        elif opcion == 2:
            dni = int(input("Ingrese DNI: ")) 
            print(">> Ejecutando inciso B...")
            mpaci.incisoB(dni, maten)
        elif opcion == 3:
            print(">> Ejecutando inciso C...")
            mpaci.incisoC(maten)
        elif opcion == 4:
            print(">> Ejecutando inciso D...")
            mpaci.incisoD()
        elif opcion == 0:
            print("Hasta luego!")
        else:
            print("Opción inválida. Intente de nuevo.")




























'''
from gestorAtencion import ManejadorAtencion
from gestorPaciente import ManejadorPaciente

def menu():
    print("-----Menu de Opciones-----")
    print("1) Informar atenciones realizas y el import total a pagar dada una fecha")
    print("2) Informar el Nombre, Apellido y cantidad de atenciones que tuvo de una persona dado su DNI")
    print("3) Listar los paciente que no han tenido atenciones")
    print("4) Listar los pacientes ordenados por Apellido de menor a mayor por unidad")
    print("0- Para finalizar")
    
if __name__ == "__main__":
    maten= ManejadorAtencion()
    mpaci= ManejadorPaciente()
    maten.cargar_atenciones()
    mpaci.cargar_pacientes()
    opcion= -1
    while opcion !=0:
        menu()
        opcion=int(input('Seleccione una opcion:'))
        if opcion == 1:
            fecha=input('Ingrese fecha')
            maten.inciso_A(fecha)
        elif opcion == 2:
            dni= input('Ingrese DNI:')
            mpaci.incisoB(dni, maten)
        elif opcion == 3:
            mpaci.incisoC(maten)
        elif opcion == 4:
            mpaci.incisoD()
        elif opcion == 0:
            print(" Hasta luego..")'''