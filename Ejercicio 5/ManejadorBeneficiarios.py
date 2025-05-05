import csv
from Beneficiario import Beneficiario
class ManejadorBeneficiario:
    __listaBeneficiarios = list
    def __init__(self):
        self.__listaBeneficiarios = []
    def agregar_beneficiario(self, unBeneficiario):
        self.__listaBeneficiarios.append(unBeneficiario)
    def cargar_beneficiarios(self):
        saltear= False
        with open("c:/Codigos Facu/2do Año/Ejercicio 5/beneficiarios.csv") as archivoBeneficiarios:
            reader= csv.reader(archivoBeneficiarios, delimiter = ';')
            bander=True
            for Benef in reader:
                if not saltear:
                    saltear=True
                else:
                    unBeneficiario=Beneficiario(int(Benef[0]),Benef[1],Benef[2],Benef[3],Benef[4],int(Benef[5]),int(Benef[6]),int(Benef[7]))
                    self.agregar_beneficiario(unBeneficiario)
        archivoBeneficiarios.close()
    def mostrarYcontar(self,idBuscar):
        i=0
        cont=0
        for i in range(len(self.__listaBeneficiarios)):
            if self.__listaBeneficiarios[i].get_idBeca() == idBuscar:
                print("Beneficiarios de dicha Beca:")
                print(self.__listaBeneficiarios[i])
                cont+= 1
            else:
                i+=1
        return cont
    
    def MostrarCantBecas(self, xdni):
        cont = 0
        encontrado = False
        for bene in self.__listaBeneficiarios:
            if bene.get_dni() == xdni:
                cont += 1
                if not encontrado:
                    nombre = bene.get_nombre()
                    apellido = bene.get_apellido()
                    encontrado = True

        if cont == 0:
            print("ERROR: DNI no registrado.")
        elif cont == 1:
            print(f"{nombre} {apellido} posee solo una beca.")
        elif cont > 1:
            print(f"{nombre} {apellido} posee {cont} becas.")      
    
    def ListarBeneficiariosMayorMenor(self):
        self.__listaBeneficiarios.sort()
        print("Beneficiarios Ordenados de Mayor a Menor por su Facultad:")
        for bene in self.__listaBeneficiarios   :
            print(bene)
            
    def ListarPromMayor8(self):
        for bene in self.__listaBeneficiarios:
            if bene.get_idBeca() != 4:
                if bene.get_promedio() > 8:
                    print(f"NyA: {bene.get_nombre()} {bene.get_apellido()} Promedio: {bene.get_promedio()}")
            