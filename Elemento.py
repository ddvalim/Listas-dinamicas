class Elemento:
    def __init__(self, numero):
        self.__numero = numero
        self.__proximo = None
    

    def get_numero(self):
        return self.__numero
    

    def get_proximo(self):
        return self.__proximo
    

    def set_proximo(self, proximo:object):
        self.__proximo = proximo