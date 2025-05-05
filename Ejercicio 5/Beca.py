class Beca:
    __idBeca: int
    __tipoBeca: str
    __importeBeca: float
    def __init__(self, idBeca, tipoBeca, importeBeca):
        self.__idBeca =idBeca
        self.__tipoBeca = tipoBeca
        self.__importeBeca = importeBeca
    def get_idBeca(self):
        return self.__idBeca
    def get_tipoBeca(self):
        return self.__tipoBeca
    def get_importeBeca(self):
        return self.__importeBeca
    def __str__(self):  
        return "ID Beca: {} Tipo Beca: {} Importe Beca: {}".format(self.__idBeca, self.__tipoBeca, self.__importeBeca)
    