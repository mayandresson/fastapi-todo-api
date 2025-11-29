#!/bin/sh
set -e

# define PORT default se não existir
: "${PORT:=8000}"

echo "Running migrations (if alembic present)..."
if command -v alembic >/dev/null 2>&1; then
  alembic upgrade head || true
fi

echo "Starting uvicorn on 0.0.0.0:${PORT}"
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --proxy-headers
