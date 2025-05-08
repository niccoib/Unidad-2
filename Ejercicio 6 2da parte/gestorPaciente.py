from paciente import Paciente
import csv
class ManejadorPaciente:
    __listapacientes: list
    
    def __init__(self):
        self.__listapacientes=[]
    
    def agregar_paciente(self,unPaciente):
        self.__listapacientes.append(unPaciente)
    
    def cargar_pacientes(self):
        archivo= open("c:/Codigos Facu/2do Año/Ejercicio 6 2da parte/pacientes.csv", encoding='utf-8')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
                paciente= Paciente(int(fila[0]), fila[1], fila[2])
                self.agregar_paciente(paciente)
                print("Paciente Cargado.")
        archivo.close()
    
    def incisoB(self,dni,maten):
        i=0
        encontrado= False
        while i < len(self.__listapacientes) and not encontrado:
            print(f"Comparando {self.__listapacientes[i].get_dni()} con {dni}")
            if self.__listapacientes[i].get_dni() == dni:
                encontrado= True
                aux=i
            else:
                i+=1
                
        if encontrado==True:
            cantAten= maten.contar_atenciones(dni)
            if cantAten == 0:
                print("La persona {} no tuvo ninguna atencion".format(self.__listapacientes[aux].get_nombre()) )
            elif cantAten == 1:
                print("La persona {} tuvo una sola atencion".format(self.__listapacientes[aux].get_nombre()) )
            elif cantAten > 1:
                print("La persona {} tuvo {} atenciones".format(self.__listapacientes[aux].get_nombre(), cantAten))
        else:
            print("Dni no encontrado.")
            
    def incisoC(self, maten):
        encontrado= False
        for paciente in self.__listapacientes:
            cantAten= maten.contar_atenciones( paciente.get_dni() )
            if cantAten == 0:
                print(paciente)
                encontrado= True
        if not encontrado:
            print("No hay ningun paciente sin antender")
    
    def incisoD(self):
        self.__listapacientes.sort()
        print("\nLista de pacientes ordenados por unidad y apellido:")
        unidadActual = ""
        for paciente in self.__listapacientes:
            if paciente.get_unidad() != unidadActual:
                unidadActual = paciente.get_unidad()
                print(f"\n----------{unidadActual}----------")
            print(f"- {paciente.get_nombre()}")
            
            
                