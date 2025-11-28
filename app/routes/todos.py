from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from app.schemas import Todo

router = APIRouter()

# armazenamento simples em memória (por simplicidade)
DB: List[Todo] = []

@router.get('/todos', response_model=List[Todo])
def list_todos():
    return DB

@router.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: str):
    for t in DB:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail='Todo not found')

@router.post('/todos', response_model=Todo, status_code=201)
def create_todo(todo: Todo):
    todo.id = str(uuid4())
    DB.append(todo)
    return todo

@router.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: str, updated: Todo):
    for i, t in enumerate(DB):
        if t.id == todo_id:
            updated.id = todo_id
            DB[i] = updated
            return updated
    raise HTTPException(status_code=404, detail='Todo not found')

@router.delete('/todos/{todo_id}', status_code=204)
def delete_todo(todo_id: str):
    for i, t in enumerate(DB):
        if t.id == todo_id:
            DB.pop(i)
            return
    raise HTTPException(status_code=404, detail='Todo not found')
