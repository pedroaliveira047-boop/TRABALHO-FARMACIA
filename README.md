# 💊 Sistema de Gestão de Medicamentos

Projeto acadêmico desenvolvido em **Python** com o objetivo de criar um sistema simples para auxiliar no cadastro e gerenciamento de medicamentos, clientes, lotes e fornecedores.

---

## 📌 Sobre o projeto

O **Sistema de Gestão de Medicamentos** foi desenvolvido como parte de um projeto acadêmico, buscando aplicar conceitos de **programação orientada a objetos, armazenamento de dados, segurança e organização de sistemas**.

O sistema permite realizar diferentes operações relacionadas ao gerenciamento de medicamentos, além de possuir recursos para controle de acesso, validação de informações e backup dos dados.

---

## 🎯 Objetivo

O principal objetivo do projeto é desenvolver uma aplicação capaz de facilitar o controle das informações de uma gestão de medicamentos, permitindo organizar os dados de forma simples e prática.

Entre as principais informações controladas estão:

* Medicamentos
* Lotes
* Validade
* Clientes
* Fornecedores
* Contas de acesso

---

## ⚙️ Funcionalidades

### 💊 Gestão de medicamentos

* Cadastro de medicamentos
* Armazenamento das informações dos medicamentos
* Consulta dos medicamentos cadastrados

### 📦 Controle de lotes

* Cadastro de lotes
* Controle da quantidade disponível
* Registro da validade
* Associação do lote ao medicamento cadastrado

### 👤 Gestão de clientes

* Cadastro de clientes
* Armazenamento dos dados dos clientes
* Proteção das senhas cadastradas

### 🔐 Controle de acesso

* Login de usuários
* Cadastro de contas
* Controle de acesso administrativo

### 🏭 Gestão de fornecedores

* Cadastro de fornecedores
* Armazenamento das informações dos fornecedores
* Gerenciamento dos fornecedores cadastrados

### 💾 Backup

* Criação de cópias dos dados cadastrados
* Identificação do backup através de data e horário

### ⚠️ Tratamento de erros

O sistema possui tratamento para situações como:

* Quantidade informada incorretamente
* Arquivo de dados inexistente
* Medicamento não cadastrado ao tentar criar um lote
* Informações inválidas inseridas pelo usuário

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Google Colab**
* **GitHub**

### Bibliotecas utilizadas

* `hashlib` — utilizada para realizar o hash das senhas
* `shutil` — utilizada para realizar cópias dos arquivos de backup
* `datetime` — utilizada para registrar data e horário dos backups
* `time` — utilizada para medir o tempo de execução de operações

---

## 🔒 Segurança

Para melhorar a segurança do sistema, as senhas não são armazenadas diretamente em texto.

É utilizado o algoritmo **SHA-256**, através da biblioteca `hashlib`, para gerar um hash da senha antes de seu armazenamento.

Dessa forma, a senha original não fica registrada diretamente no arquivo de dados.

---

## 💾 Sistema de Backup

O projeto possui uma função responsável pela realização de backups dos dados.

Antes de criar o backup, os dados são salvos e, em seguida, uma cópia do arquivo é criada.

Os arquivos de backup recebem uma identificação baseada na data e no horário em que foram criados.

Exemplo:

```text
backup_20260923_103015.txt
```

---

## 📊 Desempenho

O sistema também possui uma medição simples do tempo de execução de determinadas operações.

Para isso, é utilizada a biblioteca `time`, permitindo verificar quanto tempo uma operação levou para ser executada.

Exemplo:

```text
Tempo da operação: 0.0004 segundos
```

---

## 🧩 Principais classes

### `Medicamento`

Responsável pelo cadastro e gerenciamento das informações dos medicamentos.

### `Lote`

Responsável pelo controle dos lotes, incluindo quantidade e validade.

### `ControleLotes`

Responsável por cadastrar e gerenciar os lotes associados aos medicamentos.

### `Cad_Cliente`

Responsável pelo cadastro e armazenamento das informações dos clientes.

### `Admin`

Responsável pelo controle administrativo, login e gerenciamento das contas.

### `Dono`

Responsável pelo cadastro e gerenciamento das informações do proprietário do sistema.

### `Fornecedor`

Responsável pelas informações relacionadas aos fornecedores.

### `GestaoFornecedores`

Responsável pelo gerenciamento dos fornecedores cadastrados.

---

## 📋 Requisitos do projeto

### Requisitos Funcionais

* **Cadastro e gestão de medicamentos**
* **Controle de validade e lotes**
* **Gestão de clientes**
* **Controle de acesso**
* **Gestão de fornecedores**

### Requisitos Não Funcionais

* **Segurança**
* **Desempenho**
* **Disponibilidade**
* **Backup**
* **Privacidade**

---

## ▶️ Como executar o projeto

### 1. Abrir o projeto

O projeto pode ser executado utilizando o **Google Colab** ou um ambiente Python compatível.

### 2. Executar as células

Execute as células do código na ordem em que aparecem no projeto.

### 3. Interagir com o sistema

Após executar o código, siga as instruções apresentadas no terminal para realizar os cadastros e operações disponíveis.

---

## 📁 Armazenamento dos dados

Os dados utilizados pelo sistema são armazenados em arquivos de texto.

O arquivo principal utilizado pelo projeto é:

```text
dados.txt
```

Os backups são armazenados com nomes baseados na data e no horário de criação.

---

## 🖥️ Estrutura geral do sistema

```text
Sistema de Gestão de Medicamentos
│
├── Medicamentos
│   └── Cadastro e gerenciamento
│
├── Lotes
│   ├── Quantidade
│   └── Validade
│
├── Clientes
│   └── Cadastro
│
├── Controle de Acesso
│   ├── Login
│   └── Contas
│
├── Fornecedores
│   └── Cadastro e gerenciamento
│
├── Segurança
│   └── Hash de senhas
│
└── Backup
    └── Cópia dos dados
```

---

## 📚 Conceitos utilizados

Durante o desenvolvimento foram utilizados conceitos de:

* Programação Orientada a Objetos (POO)
* Classes e objetos
* Métodos e atributos
* Encapsulamento
* Manipulação de arquivos
* Tratamento de exceções
* Hash de senhas
* Criação de backups
* Medição de desempenho

---

## 🎓 Finalidade acadêmica

Este projeto foi desenvolvido com finalidade **acadêmica**, buscando colocar em prática os conhecimentos adquiridos durante a disciplina e demonstrar a aplicação dos conceitos de programação e desenvolvimento de sistemas.

---

## 👥 Integrantes

**Nome dos integrantes do grupo:**

* Pedro
* Willian
* Paloma

---

## 📌 Status do projeto

**Concluído / Em desenvolvimento**

> Projeto acadêmico desenvolvido em Python para gerenciamento de medicamentos.

