class Accidente:
    __tabla:list
    
    def __init__(self):
        self.__tabla=[[]]
    
    def inicializar(self,filas=19,columnas=12):  #Se coloca el numero porque ya se sabe por el enunciado
        for i in range(filas):
            for j in range(columnas):
                self.__tabla[i][j]=0
                
    def cargartabla(self,mes,dpto,cant):
        self.__tabla[dpto-1][mes-1] += cant #Menos uno porque internamente los indices se manejan como n-1
        
        