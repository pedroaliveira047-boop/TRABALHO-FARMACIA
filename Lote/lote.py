class ControleLotes:
    def __init__(self, gestao_medicamentos):
        self.lotes = []
        self.gestao_medicamentos = gestao_medicamentos

    def cadastrar(self):
        print("\n===== CADASTRAR LOTE =====")

        nome_medicamento = input("Nome do medicamento: ")

        medicamento_encontrado = None

        for medicamento in self.gestao_medicamentos.medicamentos:
            if medicamento.nome.lower() == nome_medicamento.lower():
                medicamento_encontrado = medicamento
                break

        if medicamento_encontrado is None:
            print("\nMedicamento não encontrado!")
            print("Cadastre o medicamento primeiro.")
            return

        numero = input("Número do lote: ")
        quantidade = int(input("Quantidade: "))

        lote = Lote(
            medicamento_encontrado,
            numero,
            quantidade
        )

        self.lotes.append(lote)

        print("\nLote cadastrado com sucesso!")

    def listar(self):
        print("\n===== LOTES CADASTRADOS =====")

        if len(self.lotes) == 0:
            print("Nenhum lote cadastrado.")
            return

        for lote in self.lotes:
            lote.exibir()

    def verificar_validade(self):
        print("\n===== CONTROLE DE VALIDADE =====")

        if len(self.lotes) == 0:
            print("Nenhum lote cadastrado.")
            return

        hoje = date.today()

        for lote in self.lotes:

            dias = (lote.validade - hoje).days

            print("\n------------------------")
            print(f"Medicamento: {lote.medicamento.nome}")
            print(f"Lote: {lote.numero}")
            print(
                f"Validade: "
                f"{lote.validade.strftime('%d/%m/%Y')}"
            )

            if dias < 0:
                print("STATUS: VENCIDO")

            elif dias <= 30:
                print("STATUS: PRÓXIMO DO VENCIMENTO")

            else:
                print("STATUS: DENTRO DA VALIDADE")

    def buscar(self):
        print("\n===== BUSCAR LOTE =====")

        numero = input("Digite o número do lote: ")

        for lote in self.lotes:

            if lote.numero == numero:
                lote.exibir()
                return

        print("Lote não encontrado.")

    def excluir(self):
        print("\n===== EXCLUIR LOTE =====")

        numero = input("Digite o número do lote: ")

        for lote in self.lotes:

            if lote.numero == numero:

                self.lotes.remove(lote)

                print("Lote excluído com sucesso!")
                return

        print("Lote não encontrado.")

controle = ControleLotes(gestao_medicamentos)

while True:

    print("\n==============================")
    print("     CONTROLE DE VALIDADE")
    print("==============================")

    print("1 - Cadastrar lote")
    print("2 - Listar lotes")
    print("3 - Verificar validade")
    print("4 - Buscar lote")
    print("5 - Excluir lote")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        controle.cadastrar()

    elif opcao == "2":
        controle.listar()

    elif opcao == "3":
        controle.verificar_validade()

    elif opcao == "4":
        controle.buscar()

    elif opcao == "5":
        controle.excluir()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")