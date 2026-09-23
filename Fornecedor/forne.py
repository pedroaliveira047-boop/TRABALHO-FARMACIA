class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print("\n-------------------------")
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")


class GestaoFornecedores:
    def __init__(self):
        self.fornecedores = []

    def cadastrar(self):
        print("\n===== CADASTRAR FORNECEDOR =====")

        nome = input("Nome da empresa: ")
        cnpj = input("CNPJ: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        fornecedor = Fornecedor(
            nome,
            cnpj,
            telefone,
            email
        )

        self.fornecedores.append(fornecedor)

        print("\nFornecedor cadastrado com sucesso!")

    def listar(self):
        print("\n===== FORNECEDORES =====")

        if len(self.fornecedores) == 0:
            print("Nenhum fornecedor cadastrado.")
            return

        for fornecedor in self.fornecedores:
            fornecedor.exibir()

    def buscar(self):
        print("\n===== BUSCAR FORNECEDOR =====")

        nome = input("Digite o nome da empresa: ")

        for fornecedor in self.fornecedores:

            if fornecedor.nome.lower() == nome.lower():
                fornecedor.exibir()
                return

        print("Fornecedor não encontrado.")

    def excluir(self):
        print("\n===== EXCLUIR FORNECEDOR =====")

        nome = input("Digite o nome da empresa: ")

        for fornecedor in self.fornecedores:

            if fornecedor.nome.lower() == nome.lower():

                self.fornecedores.remove(fornecedor)

                print("Fornecedor excluído com sucesso!")
                return

        print("Fornecedor não encontrado.")


