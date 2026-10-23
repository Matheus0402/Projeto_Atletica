# Projeto Atlética

Sistema em Python, executado no terminal, para controlar o empréstimo de
equipamentos da Atlética (bolas, coletes, raquetes e bicicletas).
Trabalho da disciplina de Programação Orientada a Objetos (Atividade A2).

**Autores:** Vinicius Kenzo Kitamura e José Matheus Cristo

## Como executar

Precisa de Python 3 (desenvolvido na versão 3.14). Não há bibliotecas para instalar.

    python main.py

## O que o sistema faz

- Cadastra usuários (nome, RA no formato a0000000 e tipo). Não aceita RA repetido.
- Estudante pode ficar com até 2 itens, e Servidor com até 4.
- Mostra os equipamentos e se estão disponíveis ou emprestados.
- Registra empréstimos com prazo por tipo de item:
  bola e colete 1 dia, raquete 2 dias, bicicleta 7 dias.
- Registra devoluções. Se houver atraso, o usuário fica bloqueado
  pelo mesmo número de dias do atraso.
- Mostra o histórico de cada usuário.

Os dados ficam só na memória: ao fechar o programa, tudo é apagado.

## Equipamentos iniciais

| Código | Item |
|--------|------|
| B01 | Bola de Futsal |
| B02 | Bola de Vôlei |
| B03 | Bola de Basquete |
| C01 | Colete |
| R01 | Raquete de Tênis de Mesa |
| BI01 | Bicicleta 01 |

## Arquivos

- `main.py`: menu e leitura de dados
- `usuario.py`: Usuario, Estudante e Servidor
- `equipamento.py`: Equipamento (abstrata), Bola, Colete, Raquete e Bicicleta
- `estoque.py`: lista de equipamentos
- `Relatorio_Execucao.pdf`: relatório de execução
