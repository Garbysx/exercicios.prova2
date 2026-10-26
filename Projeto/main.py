from ED.pilha import Pilha

#escreva um programa que leia um numero inteiro via texto
# ex: 140
#e converta o mesmo em um inteiro sem usar função de conversão int()

def inteiro(texto):
    algarismos = Pilha() #guarda os algarismos
    
    for c in texto:
        if c.isdigit():
            algarismos.push(c)
        else:
            raise ValueError("Valor incompatível com inteiro")

    base = 0
    num = 0
    while not algarismos.esta_vazia():
        num = num + int(algarismos.pop())*(10**base)
        base = base+1

    return num
    

#main
try:
    num = inteiro(input("Digite um número"))
except ValueError as e:
    print(f"Erro:{e}")


    




