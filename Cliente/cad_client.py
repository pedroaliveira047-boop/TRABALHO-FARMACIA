print("===== SISTEMA DE CADASTRO ====")

cliente = Cad_Cliente()

esc = input(
    "\nO que deseja fazer?"
    "\n1 - Cadastrar"
    "\n2 - Exibir"
    "\n3 - Editar"
    "\n\nEscolha: "
)

if esc == "1":

    nome = input("Digite seu nome: ")
    ano = input("Digite seu ano de nascimento: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")

    cliente.cadastrar(
        nome,
        ano,
        senha,
        cpf,
        email,
        telefone
    )

    print("\nUsuário cadastrado com sucesso!")

elif esc == "2":

    cliente.exibir_dados()

elif esc == "3":

    cliente.editar()

else:

    print("Opção inválida!")

fazer_backup(cliente)

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()



def fazer_backup(cliente_obj):
    data = datetime.now().strftime("%Y%m%d_%H%M%S")
    cliente_obj.salvar()
    shutil.copy("dados.txt", f"backup_{data}.txt")

# Gestão de usuários
class Cad_Cliente:
    def __init__(self):
        self.__nome = ""
        self.__nasc = ""
        self.__senha = ""
        self.__cpf = ""
        self.__email = ""
        self.__telefone = ""

    def cadastrar(self, nome, nasc, senha, cpf, email, telefone):
        self.__nome = nome
        self.__nasc = nasc
        self.__senha = criptografar_senha(senha)  # Criptografa a senha aqui
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone

        self.salvar()

    def salvar(self):
        with open("dados.txt", "w") as arquivo:
            arquivo.write(f"{self.__nome}\n")
            arquivo.write(f"{self.__nasc}\n")
            arquivo.write(f"{self.__senha}\n")
            arquivo.write(f"{self.__cpf}\n")
            arquivo.write(f"{self.__email}\n")
            arquivo.write(f"{self.__telefone}\n")

    def carregar(self):
        try:
            with open("dados.txt", "r") as arquivo:
                dados = arquivo.readlines()

                self.__nome = dados[0].strip()
                self.__nasc = dados[1].strip()
                self.__senha = dados[2].strip()
                self.__cpf = dados[3].strip()
                self.__email = dados[4].strip()
                self.__telefone = dados[5].strip()

                return True

        except FileNotFoundError:
            print("Nenhum cliente cadastrado ainda.")
            return False

    def exibir_dados(self):
        if self.carregar():

            print("\n===== DADOS DO CLIENTE =====")
            print(f"Nome: {self.__nome}")
            print(f"Nascimento: {self.__nasc}")
            print(f"CPF: ***.***.{self.__cpf[-5:]}")
            print(f"Email: {self.__email}")
            print(f"Telefone: {self.__telefone}")

    def editar(self):


        if not self.carregar():
            return

        print("\n===== DADOS ATUAIS =====")
        print(f"1 - Nome: {self.__nome}")
        print(f"2 - Nascimento: {self.__nasc}")
        print(f"3 - Senha: {self.__senha}")
        print(f"4 - CPF: {self.__cpf}")
        print(f"5 - Email: {self.__email}")
        print(f"6 - Telefone: {self.__telefone}")

        while True:

            acao = input(
                "\nQual dado quer editar? "
                "\n1 - Nome"
                "\n2 - Nascimento"
                "\n3 - Senha"
                "\n4 - CPF"
                "\n5 - Email"
                "\n6 - Telefone"
                "\n7 - Voltar"
                "\n\nEscolha: "
            )

            if acao == "1":
                novo = input("Digite o novo nome: ")
                self.__nome = novo
                self.salvar()
                print("Nome alterado com sucesso!")
                break

            elif acao == "2":
                novo = input("Digite o novo ano de nascimento: ")
                self.__nasc = novo
                self.salvar()
                print("Nascimento alterado com sucesso!")
                break

            elif acao == "3":
                nova_senha = input("Digite a nova senha: ")
                self.__senha = criptografar_senha(nova_senha)  # Criptografa a nova senha
                self.salvar()
                print("Senha alterada com sucesso!")
                break

            elif acao == "4":
                novo_cpf = input("Digite o novo CPF: ")
                self.__cpf = novo_cpf
                self.salvar()
                print("CPF alterado com sucesso!")
                break

            elif acao == "5":
                novo_email = input("Digite o novo email: ")
                self.__email = novo_email
                self.salvar()
                print("Email alterado com sucesso!")
                break

            elif acao == "6":
                novo_telefone = input("Digite o novo telefone: ")
                self.__telefone = novo_telefone
                self.salvar()
                print("Telefone alterado com sucesso!")
                break

            elif acao == "7":
                break

            else:
                print("Opção inválida!")