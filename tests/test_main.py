from fastapi.testclient import TestClient
import main as app_main

client = TestClient(app_main.app)

def test_empty_list():
    resp = client.get('/todos')
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_create_and_get():
    payload = {'title': 'teste', 'description': 'x', 'done': False}
    r = client.post('/todos', json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data['title'] == 'teste'
    todo_id = data['id']
    g = client.get(f'/todos/{todo_id}')
    assert g.status_code == 200
    assert g.json()['id'] == todo_id
