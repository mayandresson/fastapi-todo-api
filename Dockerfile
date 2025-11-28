# Dockerfile para FastAPI (produção)
FROM python:3.10-slim

# evitar gerar pyc e setar diretório de trabalho
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# instalar dependências de sistema se necessário
RUN apt-get update && apt-get install -y build-essential gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements e instalar (cache layer)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# copiar código
COPY . /app

# expor porta uvicorn
EXPOSE 8000

# comando padrão (usar Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
