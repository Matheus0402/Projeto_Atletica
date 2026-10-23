from datetime import date, timedelta #esse timedelta eh pra somar dias a uma data



class Usuario:
    def __init__(self, nome, matricula, tipo):
        self.nome = nome
        self.matricula = matricula
        self.tipo = tipo # isso serve pra distinguir entre usuario e servidor    
        self.data_fim_bloqueio = None
        self.itens_emprestados = []
        self.historico = []

    def limite_itens(self):
        return 0

    def pode_pegar(self):
        return len(self.itens_emprestados) < self.limite_itens()

    
    def esta_bloqueado(self):
        if self.data_fim_bloqueio is None:
            return False

        return date.today() < self.data_fim_bloqueio


    def bloquear_por_atraso(self, dias_atraso):
        if dias_atraso > 0:
            self.data_fim_bloqueio = date.today() + timedelta(days=dias_atraso)


class Estudante(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula, "Estudante")

    def limite_itens(self):
        return 2


class Servidor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula, "Servidor")

    def limite_itens(self):
        return 4
