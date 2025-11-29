#!/bin/sh
# garante valor padrão se PORT for vazio/unset
: "${PORT:=8000}"

# log simples para debugar (opcional)
echo "Starting uvicorn on 0.0.0.0:${PORT}"

# substitui o processo do shell pelo uvicorn (melhor para signals)
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
