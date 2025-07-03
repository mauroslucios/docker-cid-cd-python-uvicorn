# Projeto FastAPI com Autenticação

Este é um projeto de exemplo utilizando FastAPI para acessar dados protegidos por autenticação. A aplicação faz login em um serviço para obter um token de acesso e utiliza esse token para acessar um endpoint protegido.

## Estrutura do Projeto

- **app/main.py**: Contém a lógica principal da aplicação, incluindo endpoints para login e acesso a dados protegidos.
- **requirements.txt**: Lista de dependências do projeto.
- **Dockerfile**: Configuração do Docker para containerizar a aplicação.
- **docker-compose.yml**: Configuração do Docker Compose para orquestrar os serviços do projeto.

## Endpoints

- **POST /login**: Realiza o login para obter o token de acesso.
- **GET /dados-protegidos**: Acessa dados protegidos usando o token de acesso.

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. **Build da imagem Docker**:
   ```bash
   docker-compose build
   ```

3. **Execute o container**:
   ```bash
   docker-compose up
   ```

4. Acesse a aplicação em `http://localhost:8000`.

## Dependências

- Python 3.11
- FastAPI
- HTTPX
- Uvicorn
- Docker

## Configuração

Para que a aplicação funcione corretamente, é necessário configurar as credenciais de `USERNAME` e `PASSWORD` no arquivo `app/main.py`.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
