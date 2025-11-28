from fastapi.testclient import TestClient
import app.main as app_main
from app.database import create_db_and_tables
import os

# garantir que usamos um DB limpo para testes localmente
# (usa o DATABASE_URL padrão: sqlite:///./dev.db)
# apagar o arquivo dev.db anterior se existir para testes determinísticos
if os.path.exists('dev.db'):
    try:
        os.remove('dev.db')
    except Exception:
        pass

# criar tabelas antes de instanciar TestClient
create_db_and_tables()

# usar TestClient como context manager para garantir startup/lifespan
with TestClient(app_main.app) as client:

    def test_list_empty():
        r = client.get('/todos')
        assert r.status_code == 200
        assert r.json() == []

    def test_create_and_get():
        payload = {'title': 'teste', 'description': 'x', 'done': False}
        r = client.post('/todos', json=payload)
        assert r.status_code == 201
        data = r.json()
        assert 'id' in data
        todo_id = data['id']

        r2 = client.get(f'/todos/{todo_id}')
        assert r2.status_code == 200
        assert r2.json()['title'] == 'teste'
