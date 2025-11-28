# FastAPI To-Do API
Projeto simples de API REST para tarefas (To-Do), feito com FastAPI.

## Funcionalidades
- Endpoints CRUD para tarefas
- Armazenamento em memória (fácil de evoluir para DB)
- Exemplos de requests com `curl`

## Requisitos
- Python 3.8+

## Como rodar localmente
1. Criar e ativar um ambiente virtual (recomendado)
   ```bash
   python -m venv .venv
   .\\.venv\\Scripts\\activate  # Windows PowerShell
   source .venv/bin/activate    # macOS / Linux
   ```
2. Instalar dependências
   ```bash
   pip install -r requirements.txt
   ```
3. Rodar o servidor
   ```bash
   uvicorn main:app --reload
   ```
4. Acesse a documentação automática em:
   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoints principais
- `GET /todos` — lista todas as tarefas
- `GET /todos/{id}` — pega tarefa por id
- `POST /todos` — cria nova tarefa
- `PUT /todos/{id}` — atualiza tarefa
- `DELETE /todos/{id}` — remove tarefa

## Comandos Git sugeridos
```bash
git init
git add .
git commit -m "feat: adicionar API FastAPI de tarefas (todo)"
git branch -M main
git remote add origin https://github.com/USERNAME/fastapi-todo-api.git
git push -u origin main
```
