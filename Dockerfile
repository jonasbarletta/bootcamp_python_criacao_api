# Escolhe a Imagem
FROM python:3.13

# Instala bibliotecas que não são padrão da Imagem python
RUN pip install poetry

# Esse comando vai pegar tudo que está na pasta + o que definimos anteriormente e jogar em uma pasta chamada app, na nova Imagem
COPY . /app

# Diretório de trabalho
WORKDIR /app

# Como estamos utilizando o poetry, temos que rodar o poetry install para instalar o que está no arquivo pyproject.toml
RUN poetry install --no-root

EXPOSE 8501

# Entrypoint é o que queremos escrever no terminal
ENTRYPOINT ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8501"]
