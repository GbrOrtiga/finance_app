# 💰 Sistema Financeiro Simplificado (API Backend)

## 📌 Descrição

Este projeto consiste em uma API backend desenvolvida com Flask para controle financeiro pessoal.

O sistema permite o cadastro de usuários, categorias e lançamentos financeiros (receitas e despesas), garantindo regras de negócio para consistência dos dados.

---

## ⚙️ Tecnologias Utilizadas

* Python
* Flask
* Flask SQLAlchemy
* Flask Migrate
* SQLite

---

## 🗂️ Estrutura do Projeto

finance_app/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── transaction.py
│   │   └── log.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── categories.py
│   │   └── transactions.py
│   └── services/
│       ├── __init__.py
│       └── transaction_service.py
├── migrations/
├── .env
├── .gitignore
├── config.py
├── run.py
└── README.md

---

## 🗄️ Estrutura do Banco de Dados

### 👤 Users

Armazena os usuários do sistema

* id (PK)
* name
* email
* created_at

---

### 📂 Categories

Categorias de transações

* id (PK)
* name
* description

---

### 💰 Transactions

Registra receitas e despesas

* id (PK)
* user_id (FK)
* category_id (FK)
* amount
* type (entrada/saida)
* description
* date

---

### 📝 Logs

Registro de ações realizadas

* id (PK)
* action
* entity
* entity_id
* timestamp

---

## 🔗 Relacionamentos

* Um usuário pode ter várias transações (1:N)
* Uma categoria pode ter várias transações (1:N)

---

## 🔗 Rotas da API

### 👤 Usuários

* GET /users/
* POST /users/
* PUT /users/<id>
* DELETE /users/<id>

---

### 📂 Categorias

* GET /categories/
* POST /categories/
* PUT /categories/<id>
* DELETE /categories/<id>

---

### 💰 Transações

* GET /transactions/
* POST /transactions/
* PUT /transactions/<id>
* DELETE /transactions/<id>

---

## ⚠️ Regras de Negócio

* O valor da transação deve ser positivo
* O tipo deve ser "entrada" ou "saida"
* Toda transação deve estar vinculada a:

  * um usuário
  * uma categoria

---

## ▶️ Como Executar o Projeto

### 1. Criar ambiente virtual

python -m venv venv

### 2. Ativar ambiente

venv\Scripts\activate

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Executar aplicação

python run.py

---

## 🧪 Testes

A API pode ser testada utilizando:

* Thunder Client (VS Code)
* Postman
* Script Python com requests

---

## 🎥 Demonstração

A aplicação pode ser demonstrada através de requisições HTTP, evidenciando:

* CRUD completo
* Regras de negócio
* Persistência no banco de dados

---

## 👨‍💻 Autor
Gabriel Ortiga Vassallo Fernández
Projeto acadêmico desenvolvido para a disciplina de desenvolvimento de Sistemas.
