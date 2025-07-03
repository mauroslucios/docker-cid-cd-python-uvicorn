# Projeto FastAPI com Autenticação

## Sobre o Projeto

Este é um projeto de exemplo de como utilizar FastAPI para criar uma API com autenticação. A aplicação utiliza o módulo `httpx` para realizar o login em um serviço e posteriormente acessar um endpoint protegido.

## Integração Contínua (CI)

Este projeto utiliza GitHub Actions para integração contínua. O workflow, localizado no diretório `.github/workflows/`, é acionado a cada `push` ou `pull request` para a branch `main` e executa as seguintes tarefas:
- Instalação de dependências.
- Análise estática de código (linting).
- Build da imagem Docker para garantir a integridade da aplicação.

1. **Clone o repositório**:
   

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
   docker build -t mauroslucios/pythonuvicorn:v1 .
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
