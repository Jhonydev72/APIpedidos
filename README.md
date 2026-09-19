# Trabalho 1 - API de Pedidos

Projeto desenvolvido para a disciplina de **Desenvolvimento de Sistemas Distribuídos** da **Universidade Paulista (UNIP)**.  
Consiste em uma API RESTful para gerenciamento de pedidos construída em **FastAPI**, com persistência em **PostgreSQL** e orquestração via **Docker Compose**.

---

## 👨‍💻 Integrante

* **Nome:** João Victor Fernandes
* **Turma:** CC7P13
* **RA:** G85035-1

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework Web:** FastAPI
* **ORM:** SQLAlchemy 2.0
* **Validação de Dados:** Pydantic v2
* **Banco de Dados:** PostgreSQL 16 (Alpine)
* **Servidor ASGI:** Uvicorn
* **Containerização:** Docker e Docker Compose

---

## 📋 Pré-requisitos

* [Git](https://git-scm.com/)
* [Docker e Docker Compose](https://www.docker.com/) instalados e em execução na máquina.

---

## 🚀 Como Executar a Aplicação

A aplicação é autocontida e reprodutível. Para clonar o repositório, subir o banco de dados e a API, execute os comandos abaixo no seu terminal:

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

# 2. Acesse a branch da entrega (se aplicável)
git checkout APIPedidos-1-final

# 3. Configure as variáveis de ambiente (opcional, já há valores padrão)
cp .env.example .env

# 4. Construa as imagens e inicie os containers
docker compose up -d --build
```

O Docker Compose inicializa:
1. O container do **PostgreSQL** (com *healthcheck* configurado).
2. O container da **API FastAPI**, aguardando o banco estar saudável antes de iniciar.

A API estará disponível para acesso em:  
👉 **http://localhost:8000**

Documentação interativa automática (Swagger UI):  
👉 **http://localhost:8000/docs**

Para acompanhar os logs da aplicação:
```bash
docker compose logs -f pedidos
```

Para parar os containers:
```bash
docker compose down
```

---

## 📌 Endpoints e Guia de Testes (Postman / cURL)

Abaixo estão os endpoints disponíveis e exemplos práticos para validação.

### 1. Criar Pedido

Calcula automaticamente o `valor_total` (`quantidade * valor_unitario`), atribui o status inicial como `CRIADO`, gera a data de criação em UTC e persiste no banco de dados.

* **Método:** `POST`
* **URL:** `http://localhost:8000/pedidos/`
* **Headers:** `Content-Type: application/json`
* **Body (raw / JSON):**
```json
{
  "cliente": "Cliente Teste",
  "produto": "Teclado Mecânico",
  "quantidade": 2,
  "valor_unitario": 150.50
}
```

* **Status Retornado:** `201 Created`
* **Exemplo de Resposta:**
```json
{
  "id": 1,
  "cliente": "Cliente Teste",
  "produto": "Teclado Mecânico",
  "quantidade": 2,
  "valor_unitario": 150.5,
  "valor_total": 301.0,
  "status": "CRIADO",
  "data_criacao": "2026-09-19T05:00:00.000000Z"
}
```

---

### 2. Consultar Pedido por ID

Busca um pedido específico pelo seu identificador único.

* **Método:** `GET`
* **URL:** `http://localhost:8000/pedidos/1` *(substitua `1` pelo ID desejado)*
* **Status Retornado:** `200 OK` (se encontrado) ou `404 Not Found` (caso não exista).
* **Exemplo de Resposta (200 OK):**
```json
{
  "id": 1,
  "cliente": "Cliente Teste",
  "produto": "Teclado Mecânico",
  "quantidade": 2,
  "valor_unitario": 150.5,
  "valor_total": 301.0,
  "status": "CRIADO",
  "data_criacao": "2026-09-19T05:00:00.000000Z"
}
```

---

### 3. Listar Todos os Pedidos

Retorna uma lista contendo todos os pedidos registrados no banco de dados.

* **Método:** `GET`
* **URL:** `http://localhost:8000/pedidos/`
* **Status Retornado:** `200 OK`
* **Exemplo de Resposta:**
```json
[
  {
    "id": 1,
    "cliente": "Cliente Teste",
    "produto": "Teclado Mecânico",
    "quantidade": 2,
    "valor_unitario": 150.5,
    "valor_total": 301.0,
    "status": "CRIADO",
    "data_criacao": "2026-09-19T05:00:00.000000Z"
  }
]
```

---

### 4. Atualizar Status do Pedido

Permite alterar exclusivamente o status de um pedido existente (ex.: `CONFIRMADO`, `CANCELADO`, `ENTREGUE`).

* **Método:** `PATCH`
* **URL:** `http://localhost:8000/pedidos/1/status` *(substitua `1` pelo ID do pedido)*
* **Headers:** `Content-Type: application/json`
* **Body (raw / JSON):**
```json
{
  "status": "CONFIRMADO"
}
```

* **Status Retornado:** `200 OK` (se atualizado) ou `404 Not Found` (se o pedido não existir).
* **Exemplo de Resposta:**
```json
{
  "id": 1,
  "cliente": "Cliente Teste",
  "produto": "Teclado Mecânico",
  "quantidade": 2,
  "valor_unitario": 150.5,
  "valor_total": 301.0,
  "status": "CONFIRMADO",
  "data_criacao": "2026-09-19T05:00:00.000000Z"
}
```

---

### 5. Verificação de Saúde (Health Check)

Verifica se a aplicação está ativa e respondendo adequadamente.

* **Método:** `GET`
* **URL:** `http://localhost:8000/health`
* **Status Retornado:** `200 OK`
* **Exemplo de Resposta:**
```json
{
  "status": "ok"
}
```

---

## 🏛️ Estrutura do Projeto

A arquitetura do projeto segue o padrão em camadas, separando responsabilidades:

```text
APIpedidos/
├── app/
│   ├── api/
│   │   └── pedidos.py          # Rotas e controladores da API
│   ├── models/
│   │   └── pedido.py           # Modelos ORM (SQLAlchemy)
│   ├── repositories/
│   │   └── pedido_repository.py# Camada de persistência e acesso a dados
│   ├── schemas/
│   │   └── pedido.py           # Schemas de validação e serialização (Pydantic)
│   ├── services/
│   │   └── pedido_service.py   # Regras de negócio e orquestração
│   ├── database.py             # Configuração da sessão e engine do banco
│   └── main.py                 # Ponto de entrada da aplicação FastAPI
├── .env.example                # Modelo de variáveis de ambiente
├── docker-compose.yml          # Definição dos serviços PostgreSQL e API
├── Dockerfile                  # Construção da imagem Docker da aplicação
├── requirements.txt            # Dependências Python
└── README.md                   # Documentação do projeto
```
