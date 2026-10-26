class Node():
    """
    Classe que implementa um nó de lista encadeada
    """
    def __init__(self,dado:any):
        self.item = dado
        self.prox = None

    def __str__(self):
        return str(self.item)