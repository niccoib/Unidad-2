from ManejadorCarrera import ManejadorC
from ManejadorFacultad import ManejadorF
def menu():
    print("\nMenu de Opciones")
    print("1. Cargar datos de las Carreras desde el archivo Carreras.csv")
    print("2. Cargar datos de las Facultades desde el archivo Facultades.csv")
    print("3. Dado el nombre de una Carrera, mostrar el nombre de la Facultad en la que se dicta")
    print("4. Mostrar la cantidad de carreras que se dictan en cada Facultad")
    print("5. Dado el nombre de una Facultad, generar un listado ordenado alfabéticamente con nombre y duración de las carreras")
    print("0. Salir")

if __name__ == '__main__':
    gf = ManejadorF()
    gc = ManejadorC()
    opcion = -1

    while opcion != 0:
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            gc.cargar_carrera()
            print("Datos de las Carreras cargados correctamente.")
        
        elif opcion == 2:
            gf.cargarFacultad()
            print("Datos de las Facultades cargados correctamente.")
        
        elif opcion == 3:
            nombre = input("Ingrese el nombre de la carrera: ")
            id = gc.buscar_carrera(nombre)
            if id != "-1":
                print(f"ID de la facultad buscada: {id}")
                nom = gf.BuscarFacultad(id)
                print(f"\nEl nombre de la facultad de la carrera ingresada es: {nom}")
            else:
                print("\nNo se encontró la carrera.")
        
        elif opcion == 4:
            print("\nCantidad de carreras por Facultad:")
            gf.MostrarFac(gc)
        
        elif opcion == 5:
            nombre_facultad = input("Ingrese el nombre de la Facultad: ")
            id_control = gf.BuscarFacNom(nombre_facultad)
            gc.listar_y_ordenar(id_control)
            
        elif opcion == 0:
            print("Saliendo del programa...")
        
        else:
            print("Opción inválida. Intente nuevamente.")
            
'''
from ManejadorCarrera import ManejadorC
from ManejadorFacultad import ManejadorF
def menu():
    print("Menu de Opciones")
    print("A")
    print("B")
    print("C")
    print("D")
    print("E")

if __name__ == '__main__':
    gf= ManejadorF()
    gc= ManejadorC()
    gf.cargarFacultad()
    gc.cargarCarrera()
    menu()
    nombre= input("Ingrese el nombre de la carrera: ")
    id= gc.buscar_carrera(nombre)
    if id != -1:
        nom=gf.BuscarFacultad(id)
        print(f"\nEl nombre de la facultad de la carrera ingresada es:{nom}")
    else:
        print("Opción inválida. Intente nuevamente.")
'''

