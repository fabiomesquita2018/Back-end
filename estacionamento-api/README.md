# 🚗 API de Estacionamento com Flask + SQLite

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 
Esta é uma API RESTful desenvolvida com Python, Flask e SQLite para gerenciar a entrada e saída de veículos em um estacionamento.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask 2.3.3
- Flask-SQLAlchemy 2.5.1
- SQLite

---

## 📦 Instalação

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.


### 1. Clone o repositório

```bash
git clone https://github.com/fabiomesquita2018/EstacionamentoRioPark/estacionamento-api.git
cd estacionamento-api
```
### 2.Crie e ative um ambiente virtual

python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS

### 3. Instale as dependências

pip install -r requirements.txt

### 3. Como executar a aplicação

python app.py

Para executar a API  basta executar:

```bash
http://127.0.0.1:5000
```
## 📌 Rotas da API

### 🔹 POST /carros - Inserir um novo carro
- **Requisição**: `POST /carros`

```
exemplo:

{
  "marca": "Toyota",
  "Placa": "ABC01234",
  "entrada": "2025-06-24 08:00:00",
  "saida": "2025-06-24 10:00:00"
  
  }
  ```
  








