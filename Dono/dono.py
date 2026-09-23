class Dono:
    def __init__(self, nome, cpf, telefone, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    def login_dono(self):
        print("\n===== LOGIN DO DONO =====")

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")

        if (nome == self.__nome and
            cpf == self.__cpf and
            telefone == self.__telefone and
            email == self.__email):

            print("\nLogin realizado com sucesso!")
            print(f"Bem-vindo, {self.__nome}!")
            return True

        print("\nDados incorretos!")
        return False

    def salvar(self):
        with open("dono.txt", "w") as arquivo:
            arquivo.write(f"{self.__nome}\n")
            arquivo.write(f"{self.__cpf}\n")
            arquivo.write(f"{self.__telefone}\n")
            arquivo.write(f"{self.__email}\n")

    def exibir_dados(self):
        print("\n===== DADOS DO DONO =====")
        print(f"Nome: {self.__nome}")
        print(f"CPF: ***.***.{self.__cpf[-5:]}")
        print(f"Telefone: {self.__telefone}")
        print(f"Email: {self.__email}")


# Criando o dono
dono = Dono(
    "William",
    "1234567",
    "3191234",
    "william@email.com"
)

# Fazendo o login
dono.login_dono()