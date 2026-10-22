
from equipamento import Equipamento, Bola, Colete, Raquete, Bicicleta


class Estoque:
    def __init__(self):
        self.equipamentos = []

    def cadastrar_iniciais(self):
        self.adicionar(Bola("B01", "Bola de Futsal", "Futsal"))
        self.adicionar(Bola("B02", "Bola de Volei", "Volei"))
        self.adicionar(Bola("B03", "Bola de Basquete", "Basquete"))
        self.adicionar(Colete("C01", "Colete Azul"))
        self.adicionar(Raquete("R01", "Raquete de Tenis de Mesa"))
        self.adicionar(Bicicleta("BI01", "Bicicleta 01"))

    def adicionar(self, equipamento):
        self.equipamentos.append(equipamento)

    def listar(self):
        print("\n--- EQUIPAMENTOS ---")

        if len(self.equipamentos) == 0:
            print("Nenhum equipamento cadastrado.")
        else:
            for item in self.equipamentos:
                status = "Disponivel" if item.disponivel else "Emprestado"
                print(
                    "Codigo:", item.codigo,
                    "| Nome:", item.nome,
                    "| Prazo:", item.prazo_dias(), "dia(s)",
                    "| Status:", status
                )

    def buscar(self, codigo):
        codigo = codigo.strip().lower()

        for item in self.equipamentos:
            if item.codigo.lower() == codigo:
                return item

        return None
