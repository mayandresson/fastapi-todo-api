from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import uuid4
from sqlmodel import select
from sqlmodel import Session

from app.models import Todo
from app.database import get_session

router = APIRouter()

@router.get('/todos', response_model=List[Todo])
def list_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@router.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: str, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@router.post('/todos', response_model=Todo, status_code=201)
def create_todo(payload: Todo, session: Session = Depends(get_session)):
    todo = Todo(**payload.dict())
    if not todo.id:
        todo.id = str(uuid4())
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: str, updated: Todo, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    todo.title = updated.title
    todo.description = updated.description
    todo.done = updated.done
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.delete('/todos/{todo_id}', status_code=204)
def delete_todo(todo_id: str, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    session.delete(todo)
    session.commit()
    return
