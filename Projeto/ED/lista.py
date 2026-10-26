from ED.node import Node

class Lista():
    """
    implementação de lista simplesmente encadeada
    """
    def __init__(self):
        #cria lista vazia
        self.cabeca = None

    def esta_vazia(self):
        if self.cabeca:
            return False
        else:
            return True

    def inserir_inicio(self,dado:any):
        novo = Node(dado)
        novo.prox = self.cabeca
        self.cabeca = novo


    def imprimir_lista(self):
        aux = self.cabeca
        while(aux):
            print(f">>\n{str(aux)}\n",end="")
            aux = aux.prox
        print("<<")

    def __str__(self):
        aux = self.cabeca
        txt = ""
        while(aux):
            txt = txt + f">>\n{str(aux)}\n"
            aux = aux.prox
        txt = txt + "<<"
        return txt

    def remover_inicio(self):
        if not self.esta_vazia():
            aux = self.cabeca
            self.cabeca = self.cabeca.prox
            del aux

    def inserir_final(self,dado):
        novo = Node(dado)
        #chegar ao final da lista
        if not self.esta_vazia():
            aux = self.cabeca
            #percorrer lista até o ultimo elemento
            while(aux.prox):
                aux = aux.prox
            aux.prox = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo

    def remover_final(self):
        if not self.esta_vazia():
            aux = self.cabeca
            ant = None
            #percorrer até o ultimo elemento
            while(aux.prox):
                ant = aux
                aux = aux.prox
            if aux != self.cabeca:
                ant.prox = None
            else:
                self.cabeca = None
            del aux

    def inserir_ordenado(self,dado):
        novo = Node(dado)
        if not self.esta_vazia():
            aux = self.cabeca
            ant = None
            if dado > self.cabeca.item:
                #percorre até achar o ponto de inserção
                while aux and dado > aux.item:
                    ant = aux
                    aux = aux.prox
                ant.prox = novo
                novo.prox = aux
            else:
                novo.prox = self.cabeca
                self.cabeca = novo
        else:
            self.cabeca = novo

    def remover_dado(self,dado_busca):
        if (not self.esta_vazia()):
            ant = None
            aux = self.cabeca
        while (aux and dado_busca != aux.item):
            ant = aux
            aux = aux.prox
        if aux:
            if aux != self.cabeca:
                ant.prox = aux.prox
        else:
            self.cabeca = self.cabeca.prox
        del aux


    def min(self):
        if self.esta_vazia():
            return None
        menor = self.cabeca.item
        aux = self.cabeca.prox
        while aux:
            if aux.item < menor:
                menor = aux.item
            aux = aux.prox
        return menor

    def max(self):
        if self.esta_vazia():
            return None
        maior = self.cabeca.item
        aux = self.cabeca.prox
        while aux:
            if aux.item > maior:
                maior = aux.item
            aux = aux.prox
        return maior

    def sum(self):
        total = 0
        aux = self.cabeca
        while aux:
            total = total + aux.item
            aux = aux.prox
        return total

    def len(self):
        qtd = 0
        aux = self.cabeca
        while aux:
            qtd = qtd + 1
            aux = aux.prox
        return qtd

    def avg(self):
        if self.esta_vazia():
            return None
        return self.sum() / self.len()

    def append(self, outra_lista):
        # copia os itens da outra lista para o final desta
        # (copia para as duas listas nao dividirem os mesmos nos)
        aux = outra_lista.cabeca
        while aux:
            self.inserir_final(aux.item)
            aux = aux.prox

    def reverse(self):
        ant = None
        aux = self.cabeca
        while aux:
            prox = aux.prox
            aux.prox = ant
            ant = aux
            aux = prox
        self.cabeca = ant
