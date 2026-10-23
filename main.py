from datetime import datetime, timedelta
from usuario import Estudante, Servidor
from estoque import Estoque

usuarios = []
estoque = Estoque()
estoque.cadastrar_iniciais()


def validar_matricula(matricula):
    # raise = "lanca" um erro: pula direto para o except de quem chamou
    if not (len(matricula) == 8
            and matricula[0] == "a"
            and matricula[1:].isdigit()):
        raise ValueError("Matricula invalida! Use o formato a0000000.")

    if buscar_usuario_por_matricula(matricula) is not None:
        raise ValueError("Ja existe um usuario com essa matricula!") 


def cadastrar_usuario():
    print("\n--- CADASTRO DE USUARIO ---")

    # Validar o nome
    while True:
        nome = input("Digite o nome: ")
        nome = nome.strip() # esse strip ele remove espaços em branco do começo e do fim do texto

        if nome == "":
            print("Nome invalido! O nome nao pode ficar vazio.")
        else:
            break

       # Validar a matricula
    while True:
        matricula = input("Digite a matricula (ex: a2669560): ")
        matricula = matricula.strip().lower()

        try:
            validar_matricula(matricula)
            break  # so chega aqui se nao deu erro
        except ValueError as erro:
            print(erro)


    # Escolher o tipo de usuario
    print("1 - Estudante")
    print("2 - Servidor")

    tipo_opcao = input("Escolha o tipo de usuario: ")

    if tipo_opcao == "1":
        usuario = Estudante(nome, matricula)
    elif tipo_opcao == "2":
        usuario = Servidor(nome, matricula)
    else:
        print("Tipo de usuario invalido!")
        return

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!")


def consultar_usuarios():
    print("\n--- USUARIOS CADASTRADOS ---")

    if len(usuarios) == 0:
        print("Nenhum usuario cadastrado.")
    else:
        for usuario in usuarios:
            print("Nome:", usuario.nome)
            print("Matricula:", usuario.matricula)
            print("Tipo:", usuario.tipo)
            print("Itens emprestados:", len(usuario.itens_emprestados), "/", usuario.limite_itens())
            print("--------------------------")


def buscar_usuario_por_matricula(matricula):
    matricula = matricula.strip().lower()

    for u in usuarios:
        if u.matricula.lower() == matricula:
            return u

    return None


def consultar_equipamentos():
    estoque.listar()



def realizar_emprestimo():
    print("\n--- REALIZAR EMPRESTIMO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario is None:
        print("Usuario nao encontrado! Cadastre o usuario primeiro.")
        return

    if usuario.esta_bloqueado():
        print("Usuario bloqueado por atraso na devolucao.")
        print(
            "Bloqueio valido ate:",
        usuario.data_fim_bloqueio.strftime("%d/%m/%Y")
    )
        return

    if not usuario.pode_pegar():
        print(
            f"O usuario {usuario.nome} ja atingiu o limite de "
            f"{usuario.limite_itens()} itens!"
        )
        return

    estoque.listar()

    codigo = input("\nDigite o codigo do equipamento desejado: ")
    item = estoque.buscar(codigo)

    if item is None:
        print("Equipamento nao encontrado.")
        return

    if not item.disponivel:
        print("Equipamento ja esta emprestado no momento.")
        return

   
    item.registrar_emprestimo()  # registra o emprestimo e calcula a data prevista automaticamente

    print(
        "Data prevista para devolucao:",
        item.data_devolucao_prevista.strftime("%d/%m/%Y") # isso aqui eh massa esse strftime para dar o padrao correto
    )

    usuario.itens_emprestados.append(item)

    data_atual = datetime.now().strftime("%d/%m/%Y")
    usuario.historico.append(
        f"Emprestimo: {item.nome} em {data_atual}"
    )

    print(
        f"Emprestimo do item '{item.nome}' realizado "
        f"para {usuario.nome} com sucesso!"
    )




def registrar_devolucao():
    print("\n--- REGISTRAR DEVOLUCAO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario is None:
        print("Usuario nao encontrado.")
        return

    codigo = input("Digite o codigo do equipamento a devolver: ")
    item = estoque.buscar(codigo)

    if item and item in usuario.itens_emprestados:

       
        data_atual = datetime.now().date()  # 1 calcular o atraso antes de registrar a devolucao
        dias_atraso = 0

        if item.data_devolucao_prevista is not None:
            dias_atraso = (
                data_atual - item.data_devolucao_prevista
            ).days

       
        if dias_atraso < 0:  # se nao estiver atrasado, nao ha penalidade com o dias_atrasos = 0
            dias_atraso = 0

       
        if item.categoria == "bicicleta": # vistoria da bicicleta
            print("\n[ VISTORIA DE BICICLETA ]")
            pneu = input("Pneus ok? (s/n): ")
            freio = input("Freios ok? (s/n): ")
            print(
                f"Vistoria registrada "
                f"(pneu: {pneu}, freio: {freio})."
            )

       
        item.realizar_devolucao() # devolucao começando
        usuario.itens_emprestados.remove(item)

        data_formatada = data_atual.strftime("%d/%m/%Y")
        usuario.historico.append(
            f"Devolucao: {item.nome} em {data_formatada}"
        )

        print("Devolucao registrada com sucesso!")

       
        if dias_atraso > 0: # atraso iniciando
            usuario.bloquear_por_atraso(dias_atraso)

            print(f"Equipamento devolvido com {dias_atraso} "
                  f"dia(s) de atraso.")
            print(f"Usuario bloqueado por {dias_atraso} dia(s).")
            print(
                "Data final do bloqueio:",
                usuario.data_fim_bloqueio.strftime("%d/%m/%Y")
            )
        else:
            print("Devolucao realizada dentro do prazo!")

    else:
        print(
            "Este equipamento nao consta na lista de "
            "emprestimos deste usuario."
        )


def consultar_historico():
    print("\n--- CONSULTAR HISTORICO ---")
    matricula = input("Digite a matricula do usuario: ")
    usuario = buscar_usuario_por_matricula(matricula)

    if usuario:
        print(f"\nHistorico de {usuario.nome}:")
        if len(usuario.historico) == 0:
            print("Nenhum registro encontrado.")
        else:
            for registro in usuario.historico:
                print("-", registro)
    else:
        print("Usuario nao encontrado.")


# --- LOOP PRINCIPAL DO MENU ---
opcao = -1

while opcao != 0:
    print("\n================================")
    print("       SISTEMA DA ATLETICA")
    print("================================")
    print("1 - Cadastrar usuario")
    print("2 - Consultar usuarios")
    print("3 - Consultar equipamentos")
    print("4 - Realizar emprestimo")
    print("5 - Registrar devolucao")
    print("6 - Consultar historico")
    print("0 - Sair do sistema")

    try:
        opcao = int(input("Escolha uma opcao: "))

    except ValueError:
        print("Opcao invalida! Digite apenas numeros.")
        continue

    if opcao == 1:
        cadastrar_usuario()

    elif opcao == 2:
        consultar_usuarios()

    elif opcao == 3:
        consultar_equipamentos()

    elif opcao == 4:
        realizar_emprestimo()

    elif opcao == 5:
        registrar_devolucao()

    elif opcao == 6:
        consultar_historico()

    elif opcao == 0:
        print("Sistema encerrado!")

    else:
        print("Opcao inexistente! Escolha uma opcao do menu.")