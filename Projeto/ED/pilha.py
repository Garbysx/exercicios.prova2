from ED.node import Node

class Pilha():
    
    def __init__(self):
        """Cria a pilha vazia"""
        self.topo = None

    def esta_vazia(self):
        return not self.topo

    def push(self,dado):
        novo = Node(dado)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if not self.esta_vazia():
            aux = self.topo
            self.topo = self.topo.prox
            dado = aux.item
            del aux
            return dado

    def top(self):
        if not self.esta_vazia():
            return self.topo.item

    def destruir(self):
        while not self.esta_vazia():
            self.pop()

    def imprimir(self):
        aux = Pilha()
        while not self.esta_vazia():
            print(self.top())
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())

    def buscar(self, info):
        aux = self.topo
        while aux:
            if aux.item == info:
                return True
            aux = aux.prox
        return False

    def editar(self, info, novo=None):
        aux = self.topo
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
        aux = self.topo
        while aux and aux.item != info:
            ant = aux
            aux = aux.prox
        if not aux:
            return False
        if ant:
            ant.prox = aux.prox
        else:
            self.topo = aux.prox
        del aux
        return True

    def remover_repetidos(self):
        atual = self.topo
        while atual:
            ant = atual
            aux = atual.prox
            while aux:
                if aux.item == atual.item:
                    ant.prox = aux.prox
                else:
                    ant = aux
                aux = aux.prox
            atual = atual.prox
