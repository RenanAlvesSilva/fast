# Fast

Projeto FastAPI para gerenciamento de lojas com cálculo de distância e categorias.

## 📋 Pré-requisitos

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/) - gerenciador de pacotes rápido para Python

## 🚀 Como Baixar e Executar

### 1. Instalar `uv`

Se você ainda não tem `uv` instalado, siga as instruções em [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

No Windows, você pode instalar via:
```bash
pip install uv
```

Ou use o instalador oficial.

### 2. Clonar o Repositório

```bash
git clone https://github.com/RenanAlvesSilva/fast.git
cd fast
```

### 3. Instalar Dependências

```bash
uv sync
```

Este comando criará um ambiente virtual (`.venv`) e instalará todas as dependências definidas no `pyproject.toml`.

### 4. Executar a Aplicação

Para executar a aplicação em modo desenvolvimento com recarga automática:

```bash
uv run uvicorn backend.routers:app --reload
```

A API estará disponível em: **http://localhost:8000**

### 5. Acessar a Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📦 Dependências Principais

- **FastAPI** (>=0.136.1) - Framework web moderno
- **SQLAlchemy** (>=2.0.49) - ORM para banco de dados
- **Geopy** (>=2.4.1) - Cálculo de distâncias geográficas
- **HTTPX** (>=0.28.1) - Cliente HTTP assíncrono

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
fast/
├── backend/
│   ├── category.py          # Lógica de categorias
│   ├── database.py          # Configuração do banco de dados
│   ├── distance_service.py  # Serviço de cálculo de distância
│   ├── models.py            # Modelos SQLAlchemy
│   ├── routers.py           # Rotas da API
│   ├── schemas.py           # Schemas Pydantic
│   ├── services.py          # Lógica de negócio
│   └── store_service.py     # Serviço de lojas
├── main.py                  # Ponto de entrada
├── pyproject.toml           # Configuração do projeto
└── README.md                # Este arquivo
```

### Ativar Ambiente Virtual (Opcional)

Se você quiser ativar o ambiente virtual manualmente:

```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

### Instalar Pacotes Adicionais

```bash
uv pip install <nome_do_pacote>
```

Ou adicione ao `pyproject.toml` e execute:
```bash
uv sync
```

## 📝 Notas

- A aplicação utiliza banco de dados SQLAlchemy
- Suporta cálculo de distâncias entre pontos geográficos
- API RESTful construída com FastAPI

## ✨ Próximos Passos

1. Configure as variáveis de ambiente se necessário
2. Configure o banco de dados
3. Crie as tabelas conforme necessário
4. Comece a desenvolver!

---

Para mais informações sobre `uv`, consulte a [documentação oficial](https://docs.astral.sh/uv/).
