
from datetime import date, timedelta


def analisar_emprestimo(data_prevista):
    hoje = date.today()

    if hoje > data_prevista:
        return "Atrasado"

    elif hoje == data_prevista:
        return "Vence hoje"

    return "Em dia"


class Equipamento:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.disponivel = True
        self.categoria = "equipamento"

        self.data_emprestimo = None
        self.data_devolucao_prevista = None
        self.data_devolucao_real = None

    def prazo_dias(self):
        return 0

    def registrar_emprestimo(self):
        self.data_emprestimo = date.today()

        prazo = self.prazo_dias()

        self.data_devolucao_prevista = (
            self.data_emprestimo + timedelta(days=prazo)
        )

        self.data_devolucao_real = None
        self.disponivel = False

    def verificar_situacao(self):
        if self.data_devolucao_real is not None:
            return "Devolvido"

        if self.data_devolucao_prevista is None:
            return "Sem prazo definido"

        return analisar_emprestimo(
            self.data_devolucao_prevista
        )

    def realizar_devolucao(self):
        self.data_devolucao_real = date.today()
        self.disponivel = True

    def realizar_vistoria(self):
        return "Este equipamento nao precisa de vistoria especial."


class Bola(Equipamento):
    def __init__(self, codigo, nome, esporte):
        super().__init__(codigo, nome)
        self.esporte = esporte
        self.categoria = "bola"

    def prazo_dias(self):
        return 1


class Colete(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.categoria = "colete"

    def prazo_dias(self):
        return 1


class Raquete(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.categoria = "raquete"

    def prazo_dias(self):
        return 2


class Bicicleta(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.categoria = "bicicleta"

    def prazo_dias(self):
        return 7

    def realizar_vistoria(self):
        return "Verificar pneus, freios e corrente."
