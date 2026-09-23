class Admin:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.nivel = "Administrador"
        self.contas = []

    def login(self):
        nome = input("Digite o nome do administrador: ")
        senha = input("Digite a senha: ")

        if nome == self.nome and senha == self.senha:
            print("\nLogin realizado com sucesso!")
            print(f"Bem-vindo, {self.nome}!")
            return True

        else:
            print("\nNome ou senha incorretos!")
            return False

    def cadastrar_conta(self):
        print("\n===== CADASTRAR CONTA ====")

        nome = input("Nome da conta: ")
        senha = input("Senha da conta: ")

        conta = {
            "nome": nome,
            "senha": senha
        }

        self.contas.append(conta)

        print("Conta cadastrada com sucesso!")

    def listar_contas(self):
        print("\n===== CONTAS CADASTRADAS ====")

        if len(self.contas) == 0:
            print("Nenhuma conta cadastrada.")
            return

        for conta in self.contas:
            print(f"Nome: {conta['nome']}")

    def deletar_conta(self):
        print("\n===== DELETAR CONTA ====")

        nome = input("Digite o nome da conta que deseja deletar: ")

        for conta in self.contas:

            if conta["nome"].lower() == nome.lower():

                self.contas.remove(conta)

                print("Conta deletada com sucesso!")
                return

        print("Conta não encontrada.")

    def exibir_dados(self):
        print("\n===== ADMINISTRADOR ====")
        print(f"Nome: {self.nome}")
        print(f"Nível de acesso: {self.nivel}")


admin = Admin("admin", "1234")
logado = False # Inicializa o status de login

while True:

    print("\n==============================")
    print("       SISTEMA ADMIN")
    print("==============================")

    print("1 - Fazer login")
    print("2 - Cadastrar conta")
    print("3 - Listar contas")
    print("4 - Deletar conta")
    print("5 - Ver dados do administrador")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        logado = admin.login() # Atualiza o status de login

    elif opcao == "2":
        if logado:
            admin.cadastrar_conta()
        else:
            print("Faça login primeiro para cadastrar uma conta.")

    elif opcao == "3":
        if logado:
            admin.listar_contas()
        else:
            print("Faça login primeiro para listar as contas.")

    elif opcao == "4":
        if logado:
            admin.deletar_conta()
        else:
            print("Faça login primeiro para deletar uma conta.")

    elif opcao == "5":
        if logado:
            admin.exibir_dados()
        else:
            print("Faça login primeiro para ver os dados do administrador.")

    elif opcao == "6":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
