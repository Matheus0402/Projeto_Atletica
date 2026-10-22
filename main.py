
from usuario import Usuario

usuarios = []

from equipamento import Equipamento

teste = Equipamento("B01", "Bola de Futsal")

print(teste.codigo)
print(teste.nome)
print(teste.disponivel)


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
    while True: # isso aqui he interessante pois ele roda uma repeticao ate encontrar um break
        matricula = input("Digite a matricula (ex: a2669560): ")

        if (len(matricula) == 8
                and matricula[0] == "a"
                and matricula[1:].isdigit()): # aqui eh pra verificar se todos os espaços apos o vetor[0]=a sao numeros
            break
        else:
            print("Matricula invalida! Use o formato a0000000.")

    # Escolher o tipo de usuario
    print("1 - Estudante")
    print("2 - Servidor")

    tipo_opcao = input("Escolha o tipo de usuario: ")

    if tipo_opcao == "1":
        tipo = "Estudante"
    elif tipo_opcao == "2":
        tipo = "Servidor"
    else:
        print("Tipo de usuario invalido!")
        return

    usuario = Usuario(nome, matricula, tipo)

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
            print("--------------------------")



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
        print("Consulta de equipamentos em desenvolvimento.")

    elif opcao == 4:
        print("Emprestimos em desenvolvimento.")

    elif opcao == 5:
        print("Devolucoes em desenvolvimento.")

    elif opcao == 6:
        print("Historico em desenvolvimento.")

    elif opcao == 0:
        print("Sistema encerrado!")

    else:
        print("Opcao inexistente! Escolha uma opcao do menu.")
