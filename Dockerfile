FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

# converter line endings do start.sh e garantir exec
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
