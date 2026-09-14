# Carros

Sistema web de gestão de estoque de veículos, feito em Django. Permite cadastrar, listar, editar e remover carros, com autenticação de usuários e geração automática de descrição de venda via API da OpenAI.

## Funcionalidades

- Cadastro, edição, exclusão e listagem de carros (marca, modelo, ano, valor, placa, foto)
- Autenticação de usuários (registro, login, logout)
- Geração automática da descrição de venda de cada carro usando a API da OpenAI (`gpt-3.5-turbo`), disparada via signal do Django ao salvar um carro sem `bio` preenchida
- Controle de inventário: contagem e valor total dos carros em estoque, atualizado automaticamente a cada criação/remoção

## Stack

- Python / Django 5.2
- PostgreSQL (produção) / SQLite (desenvolvimento)
- OpenAI API
- Pillow (upload de imagens)

## Como rodar localmente

1. Clone o repositório e crie um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Copie `.env.example` para `.env` e preencha os valores (a chave da OpenAI é opcional — sem ela, a geração automática de descrição não funciona, mas o resto do sistema roda normalmente):

   ```bash
   copy .env.example .env
   ```

4. Rode as migrações e suba o servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Variáveis de ambiente

Veja `.env.example` para a lista completa. As principais:

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True`/`False` |
| `DB_*` | Credenciais do PostgreSQL |
| `OPENAI_API_KEY` | Chave da API da OpenAI, usada para gerar a descrição dos carros |

## Licença

Este projeto está sob a licença MIT — veja [LICENSE](LICENSE).
