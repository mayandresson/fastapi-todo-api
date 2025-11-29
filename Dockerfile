FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# copiar requirements e instalar primeiro (cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

# copiar o código
COPY . /app

EXPOSE 8000

ENV PORT 8000

# comando de arranque: usar sh -c (expande )
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port "]
