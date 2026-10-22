
class Usuario:
    def __init__(self, nome, matricula, tipo):
        self.nome = nome
        self.matricula = matricula
        self.tipo = tipo # isso aqui servira para distinguir entre usuario e servidor
