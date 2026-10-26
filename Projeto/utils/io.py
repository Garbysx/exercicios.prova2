#tarefa fazer a validação de positivo para o ler inteiro
import os

def ler_texto(msg="",campo="campo"):
    while(True):
        var = input(msg)
        if (len(var)>0):
            return var
        else:
            print(f"Digite valor de {campo} válido(a)...")


def ler_inteiro(msg="",positivo = False):
    while(True):
            try:
                var = int(input(msg))
                if positivo and var>=0:
                    return var
                elif not positivo:
                    return var
                else:
                    raise ValueError
            except:
                print("Entrada inválida! Digite um valor inteiro...")

def ler_decimal(msg="",positivo=False):
    while(True):
        try:
            var = float(input(msg))
            if positivo and var>=0:
                return var
            elif not positivo:
                return var
            else:
                raise ValueError
        except:
            print("Entrada inválida! Digite um valor decimal...")

def limpar_tela():
    input("pressione enter para continuar...")
    os.system("cls")

