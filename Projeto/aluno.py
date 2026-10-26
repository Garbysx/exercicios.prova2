from utils.io import *

class Aluno:
    """ classe que implementa um aluno de academia básico
    """
    def __init__(self,nome="",idade=1,peso=1,altura=1,id=0):
        """construtor parametrizado"""
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.id = id
        self.imc = self.calc_imc()

    def ler_dados(self):
        self.nome = ler_texto("Nome:",campo="nome")
        self.idade = ler_inteiro("Idade:",positivo=True)
        self.peso = ler_decimal("Peso:",positivo=True)
        self.altura = ler_decimal("Altura:",positivo=True)
        self.imc = self.calc_imc()

    def __str__(self):
        texto = f"""Aluno id: {self.id}
    Nome: {self.nome}
    Idade: {self.idade}
    Peso: {self.peso:.1f}
    Altura: {self.altura:.2f}
    IMC: {self.imc:.1f}
"""
        return texto

    def calc_imc(self):
        self.imc = self.peso/(self.altura**2)
        return self.imc

    def __ge__(self, outro):
        return self.nome >= outro.nome

    def __gt__(self, outro):
        return self.nome >= outro.nome

