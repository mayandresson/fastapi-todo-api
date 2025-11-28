from fastapi.testclient import TestClient
import app.main as app_main

client = TestClient(app_main.app)

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
