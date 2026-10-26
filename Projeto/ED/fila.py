from ED.node import Node

class Fila():

    def __init__(self):
        self.inicio = None
        self.final = None

    def esta_vazia(self):
        return not self.inicio

    def enqueue(self,dado):
        novo = Node(dado)
        if not self.esta_vazia():
            self.final.prox = novo
            self.final = novo
        else:
            self.inicio = novo
            self.final = novo

    def dequeue(self):
        aux = self.inicio
        if not self.esta_vazia():
            if self.inicio != self.final:
                self.inicio = self.inicio.prox
            else:
                self.inicio = None
                self.final = None
            dado = aux.item
            del aux
            return dado

    def first(self):
        if not self.esta_vazia():
            return self.inicio.item

    def destruir(self):
        while not self.esta_vazia():
            self.dequeue()

    def imprimir(self):
        aux = Fila()
        while not self.esta_vazia():
            print(self.first())
            aux.enqueue(self.dequeue())

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())

    def imprimir_fila(self):
        aux = self.inicio
        while aux:
            print(aux.item)
            aux = aux.prox

    def buscar(self, info):
        aux = self.inicio
        while aux:
            if aux.item == info:
                return True
            aux = aux.prox
        return False

    def editar(self, info, novo=None):
        aux = self.inicio
        while aux:
            if aux.item == info:
                if novo is None:
                    novo = input("Novo valor: ")
                aux.item = novo
                return True
            aux = aux.prox
        return False

    def remover(self, info):
        ant = None
        aux = self.inicio
        while aux and aux.item != info:
            ant = aux
            aux = aux.prox
        if not aux:
            return False
        if ant:
            ant.prox = aux.prox
        else:
            self.inicio = aux.prox
        if aux == self.final:
            self.final = ant
        del aux
        return True

    def remover_repetidos(self):
        atual = self.inicio
        while atual:
            ant = atual
            aux = atual.prox
            while aux:
                if aux.item == atual.item:
                    ant.prox = aux.prox
                    if aux == self.final:
                        self.final = ant
                else:
                    ant = aux
                aux = aux.prox
            atual = atual.prox
