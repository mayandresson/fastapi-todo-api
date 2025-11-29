FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# copiar requirements e instalar primeiro (cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

# copiar o código (inclui start.sh)
COPY . /app

# garantir linhas finais e permissions; chmod no build
RUN chmod +x /app/start.sh || true

EXPOSE 8000

# Deixe PORT padrão (mas Render sobrescreve)
ENV PORT 8000

# start script robusto
CMD ["/app/start.sh"]
