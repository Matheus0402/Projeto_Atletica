from datetime import date, timedelta
from abc import ABC, abstractmethod


def analisar_emprestimo(data_prevista):
    hoje = date.today()

    if hoje > data_prevista:
        return "Atrasado"

    elif hoje == data_prevista:
        return "Vencimento Proximo"

    return "Em dia"


class Equipamento(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__disponivel = True
        self.__categoria = "equipamento"

        self.__data_emprestimo = None
        self.__data_devolucao_prevista = None
        self.__data_devolucao_real = None

    @abstractmethod
    def prazo_dias(self):
        pass

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def disponivel(self):
        return self.__disponivel

    @property
    def categoria(self):
        return self.__categoria

    @property
    def data_emprestimo(self):
        return self.__data_emprestimo

    @property
    def data_devolucao_prevista(self):
        return self.__data_devolucao_prevista

    @property
    def data_devolucao_real(self):
        return self.__data_devolucao_real

    def _definir_categoria(self, categoria):
        self.__categoria = categoria

 
    def registrar_emprestimo(self):
        self.__data_emprestimo = date.today()

        prazo = self.prazo_dias()

        self.__data_devolucao_prevista = (
            self.__data_emprestimo + timedelta(days=prazo) # isso aqui eh massa hein
        )

        self.__data_devolucao_real = None
        self.__disponivel = False

    def verificar_situacao(self):
        if self.__data_devolucao_real is not None:
            return "Devolvido"

        if self.__data_devolucao_prevista is None:
            return "Sem prazo definido"

        return analisar_emprestimo(
            self.__data_devolucao_prevista
        )

    def realizar_devolucao(self):
        self.__data_devolucao_real = date.today()
        self.__disponivel = True


    def realizar_vistoria(self):
        return "Este equipamento nao precisa de vistoria especial."


class Bola(Equipamento):
    def __init__(self, codigo, nome, esporte):
        super().__init__(codigo, nome)
        self.esporte = esporte
        self._definir_categoria("bola")

    def prazo_dias(self):
        return 1


class Colete(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._definir_categoria("colete")

    def prazo_dias(self):
        return 1


class Raquete(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._definir_categoria("raquete")

    def prazo_dias(self):
        return 2


class Bicicleta(Equipamento):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self._definir_categoria("bicicleta")

    def prazo_dias(self):
        return 7

    def realizar_vistoria(self):
        return "Verificar pneus, freios e corrente."
