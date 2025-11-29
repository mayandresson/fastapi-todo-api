FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# copiar requirements e instalar primeiro (melhora cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

# copiar todo o código
COPY . /app

# instalar dos2unix para garantir conversão de CRLF -> LF e remover BOM, depois cleanup
RUN apt-get update \
 && apt-get install -y --no-install-recommends dos2unix \
 && dos2unix /app/start.sh || true \
 && chmod +x /app/start.sh \
 && apt-get remove -y dos2unix \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
ENV PORT 8000

CMD ["/app/start.sh"]
