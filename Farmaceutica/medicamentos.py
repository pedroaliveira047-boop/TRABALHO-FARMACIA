class Medicamento:
    def __init__(self, nome, principio_ativo, fabricante):
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.fabricante = fabricante

    def exibir(self):
        print("\n===== MEDICAMENTO =====")
        print(f"Nome: {self.nome}")
        print(f"Princípio ativo: {self.principio_ativo}")
        print(f"Fabricante: {self.fabricante}")


class GestaoMedicamentos:
    def __init__(self):
        self.medicamentos = []

    def cadastrar(self):
        print("\n===== CADASTRAR MEDICAMENTO =====")

        nome = input("Nome do medicamento: ")
        principio_ativo = input("Princípio ativo: ")
        fabricante = input("Fabricante: ")

        medicamento = Medicamento(
            nome,
            principio_ativo,
            fabricante
        )

        self.medicamentos.append(medicamento)

        print("\nMedicamento cadastrado com sucesso!")

    def listar(self):
        print("\n===== MEDICAMENTOS CADASTRADOS =====")

        if len(self.medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")
            return

        for medicamento in self.medicamentos:
            medicamento.exibir()

    def buscar(self):
        print("\n===== BUSCAR MEDICAMENTO =====")

        nome = input("Digite o nome do medicamento: ")

        for medicamento in self.medicamentos:
            if medicamento.nome.lower() == nome.lower():
                medicamento.exibir()
                return

        print("Medicamento não encontrado.")

    def excluir(self):
        print("\n===== EXCLUIR MEDICAMENTO =====")

        nome = input("Digite o nome do medicamento: ")

        for medicamento in self.medicamentos:
            if medicamento.nome.lower() == nome.lower():
                self.medicamentos.remove(medicamento)
                print("Medicamento excluído com sucesso!")
                return

        print("Medicamento não encontrado.")


gestao_medicamentos = GestaoMedicamentos()


while True:
    print("\n==============================")
    print("    GESTÃO DE MEDICAMENTOS")
    print("==============================")

    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Excluir medicamento")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        gestao_medicamentos.cadastrar()

    elif opcao == "2":
        gestao_medicamentos.listar()

    elif opcao == "3":
        gestao_medicamentos.buscar()

    elif opcao == "4":
        gestao_medicamentos.excluir()

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")