from Elemento import Elemento

class Lista:
    def __init__(self):
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__numero_elementos = 0


    def lista_vazia(self):
        return self.__numero_elementos == 0
    

    def insere_elemento(self, elemento:object):
        if isinstance(elemento, Elemento):
            if self.lista_vazia() == True:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__numero_elementos += 1
            else:
                self.__ultimo_elemento.set_proximo(elemento)
                self.__ultimo_elemento = elemento
                self.__numero_elementos += 1
        else:
            raise Exception('O parâmetro deve ser do tipo Elemento!')


    def remove_elemento(self, elemento:object):
        if elemento == self.__primeiro_elemento:
            temp = self.__primeiro_elemento.get_proximo()
            self.__primeiro_elemento = temp
            self.__numero_elementos -= 1
            return ('Elemento removido!')

        elif elemento == self.__ultimo_elemento:
            i = self.__primeiro_elemento
            while i.get_proximo() != self.__ultimo_elemento:
                i = i.get_proximo()
            
            self.__ultimo_elemento = i
            i.set_proximo(None)
            return ('Elemento removido!')

        else:
            i = self.__primeiro_elemento
            while i.get_proximo() != elemento:
                if i == None:
                    raise Exception('O elemento não está na lista!')
                else:
                    i = i.get_proximo()

            temp = i.get_proximo()
            nova_ref = temp.get_proximo()

            i.set_proximo(nova_ref)
            self.__numero_elementos -= 1
            return temp

    def consulta_por_elemento(self, elemento:object):
        if isinstance(elemento, Elemento):
            if elemento == self.__primeiro_elemento or elemento == self.__ultimo_elemento:
                return True
            else:
                i = self.__primeiro_elemento
                while i != elemento:
                    if i == None:
                        raise Exception ('O elemento não está na lista!')
                    else:
                        i = i.__get_proximo()
                return i == elemento
    
    def consulta_por_posicao(self, posicao:int):
        i = self.__primeiro_elemento
        for x in range(posicao):
            i = i.get_proximo()
        return i.get_numero()

l = Lista()
e = Elemento(2)
f = Elemento(3)
g = Elemento(4)
h = Elemento(5)
j = Elemento(6)

l.insere_elemento(e)
l.insere_elemento(f)
l.insere_elemento(g)
l.insere_elemento(h)

print(l.consulta_por_elemento(e))
print(l.consulta_por_posicao(1))

l.remove_elemento(h)
print(l.consulta_por_elemento(h)) #Está crashando ao consultar elemento inexistente
l.remove_elemento(h) #Está crashando ao remover elemento inexistente
