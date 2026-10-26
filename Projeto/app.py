from ED.lista import Lista
from ED.pilha import Pilha
from ED.fila import Fila


def montar_lista(valores):
    l = Lista()
    for v in valores:
        l.inserir_final(v)
    return l


def lista_para_py(l):
    itens = []
    aux = l.cabeca
    while aux:
        itens.append(aux.item)
        aux = aux.prox
    return itens


def pilha_para_py(p):
    # do topo para a base
    itens = []
    aux = p.topo
    while aux:
        itens.append(aux.item)
        aux = aux.prox
    return itens


def fila_para_py(f):
    # do inicio para o final
    itens = []
    aux = f.inicio
    while aux:
        itens.append(aux.item)
        aux = aux.prox
    return itens


def testar(nome, obtido, esperado):
    status = "OK  " if obtido == esperado else "ERRO"
    print(f"[{status}] {nome}: obtido={obtido} esperado={esperado}")


# ---------------- 1. percurso em lista ----------------
print("=== LISTA: percurso ===")
l = montar_lista([5, 2, 9, 1, 7])
testar("min", l.min(), 1)
testar("max", l.max(), 9)
testar("sum", l.sum(), 24)
testar("avg", l.avg(), 4.8)
testar("len", l.len(), 5)

vazia = Lista()
testar("min vazia", vazia.min(), None)
testar("max vazia", vazia.max(), None)
testar("sum vazia", vazia.sum(), 0)
testar("avg vazia", vazia.avg(), None)
testar("len vazia", vazia.len(), 0)

# ---------------- 2. gerais de lista ----------------
print("\n=== LISTA: gerais ===")
a = montar_lista([1, 2, 3])
b = montar_lista([4, 5])
a.append(b)
testar("append", lista_para_py(a), [1, 2, 3, 4, 5])
testar("append (b nao muda)", lista_para_py(b), [4, 5])

b.inserir_final(6)
testar("append (a independente de b)", lista_para_py(a), [1, 2, 3, 4, 5])

c = Lista()
c.append(montar_lista([8, 9]))
testar("append em lista vazia", lista_para_py(c), [8, 9])

d = montar_lista([1, 2, 3, 4])
d.reverse()
testar("reverse", lista_para_py(d), [4, 3, 2, 1])
d.inserir_final(0)
testar("reverse + inserir_final", lista_para_py(d), [4, 3, 2, 1, 0])

e = Lista()
e.reverse()
testar("reverse vazia", lista_para_py(e), [])

f = montar_lista([1])
f.reverse()
testar("reverse 1 elemento", lista_para_py(f), [1])

# ---------------- 3. pilha ----------------
print("\n=== PILHA ===")
p = Pilha()
for v in [1, 2, 3, 2, 4, 1]:
    p.push(v)
# topo -> base: 1 4 2 3 2 1
testar("pilha inicial", pilha_para_py(p), [1, 4, 2, 3, 2, 1])
testar("buscar existe", p.buscar(3), True)
testar("buscar nao existe", p.buscar(99), False)

testar("editar retorno", p.editar(3, 30), True)
testar("editar resultado", pilha_para_py(p), [1, 4, 2, 30, 2, 1])
testar("editar inexistente", p.editar(99, 0), False)

testar("remover do meio", p.remover(30), True)
testar("remover resultado", pilha_para_py(p), [1, 4, 2, 2, 1])
testar("remover topo", p.remover(1), True)
testar("remover topo resultado", pilha_para_py(p), [4, 2, 2, 1])
testar("remover inexistente", p.remover(99), False)

p.remover_repetidos()
testar("remover_repetidos", pilha_para_py(p), [4, 2, 1])

p2 = Pilha()
p2.remover_repetidos()
testar("pilha vazia remover_repetidos", pilha_para_py(p2), [])
testar("pilha vazia buscar", p2.buscar(1), False)
testar("pilha vazia remover", p2.remover(1), False)

# ---------------- 4. fila ----------------
print("\n=== FILA ===")
q = Fila()
for v in [1, 2, 3, 2, 4, 1]:
    q.enqueue(v)
print("imprimir_fila:")
q.imprimir_fila()
testar("fila inicial", fila_para_py(q), [1, 2, 3, 2, 4, 1])
testar("buscar existe", q.buscar(4), True)
testar("buscar nao existe", q.buscar(99), False)

testar("editar retorno", q.editar(4, 40), True)
testar("editar resultado", fila_para_py(q), [1, 2, 3, 2, 40, 1])
testar("editar inexistente", q.editar(99, 0), False)

testar("remover do meio", q.remover(40), True)
testar("remover resultado", fila_para_py(q), [1, 2, 3, 2, 1])
testar("remover do final", q.remover(1) and q.remover(1), True)
testar("remover resultado", fila_para_py(q), [2, 3, 2])
testar("remover inexistente", q.remover(99), False)

q.remover_repetidos()
testar("remover_repetidos", fila_para_py(q), [2, 3])

# o ponteiro final precisa continuar certo
q.enqueue(7)
testar("enqueue apos remocoes", fila_para_py(q), [2, 3, 7])

q3 = Fila()
for v in [5, 5, 5]:
    q3.enqueue(v)
q3.remover_repetidos()
q3.enqueue(6)
testar("repetidos no final + enqueue", fila_para_py(q3), [5, 6])

q4 = Fila()
q4.enqueue(1)
q4.remover(1)
q4.enqueue(2)
testar("remover unico + enqueue", fila_para_py(q4), [2])
testar("dequeue", q4.dequeue(), 2)

q5 = Fila()
testar("fila vazia buscar", q5.buscar(1), False)
testar("fila vazia remover", q5.remover(1), False)
q5.remover_repetidos()
q5.imprimir_fila()
