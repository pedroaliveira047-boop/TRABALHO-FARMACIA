import streamlit as st

st.set_page_config(
    page_title="Sistema de Gestão de Medicamentos",
    page_icon="💊"
)

st.title("💊 Sistema de Gestão de Medicamentos")

st.write(
    "Sistema desenvolvido para gerenciamento "
    "de medicamentos, clientes, lotes e fornecedores."
)

st.sidebar.title("Menu")

opcao = st.sidebar.selectbox(
    "Escolha uma opção:",
    [
        "Início",
        "Medicamentos",
        "Clientes",
        "Lotes",
        "Fornecedores",
        "Administração"
    ]
)

if opcao == "Início":

    st.header("Bem-vindo ao sistema!")

    st.write(
        "Utilize o menu ao lado para acessar "
        "as funcionalidades do sistema."
    )


elif opcao == "Medicamentos":

    st.header("💊 Gestão de Medicamentos")

    nome = st.text_input("Nome do medicamento")
    principio = st.text_input("Princípio ativo")
    fabricante = st.text_input("Fabricante")

    if st.button("Cadastrar medicamento"):

        if nome and principio and fabricante:
            st.success("Medicamento cadastrado com sucesso!")

        else:
            st.warning("Preencha todos os campos.")


elif opcao == "Clientes":

    st.header("👤 Gestão de Clientes")

    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    email = st.text_input("Email")

    if st.button("Cadastrar cliente"):

        if nome and cpf and email:
            st.success("Cliente cadastrado com sucesso!")

        else:
            st.warning("Preencha todos os campos.")


elif opcao == "Lotes":

    st.header("📦 Controle de Lotes")

    medicamento = st.text_input("Medicamento")
    numero = st.text_input("Número do lote")
    quantidade = st.number_input(
        "Quantidade",
        min_value=0,
        step=1
    )

    if st.button("Cadastrar lote"):

        if medicamento and numero:
            st.success("Lote cadastrado com sucesso!")

        else:
            st.warning("Preencha os campos.")


elif opcao == "Fornecedores":

    st.header("🏭 Gestão de Fornecedores")

    nome = st.text_input("Nome da empresa")
    cnpj = st.text_input("CNPJ")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")

    if st.button("Cadastrar fornecedor"):

        if nome and cnpj and telefone and email:
            st.success("Fornecedor cadastrado com sucesso!")

        else:
            st.warning("Preencha todos os campos.")


elif opcao == "Administração":

    st.header("🔐 Administração")

    nome = st.text_input("Nome do administrador")
    senha = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Entrar"):

        if nome == "admin" and senha == "1234":

            st.success("Login realizado com sucesso!")

        else:

            st.error("Nome ou senha incorretos.")