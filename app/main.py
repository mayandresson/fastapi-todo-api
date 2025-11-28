from fastapi import FastAPI
from app.routes.todos import router as todos_router
from app.database import create_db_and_tables

app = FastAPI(title='To-Do API', version='0.1.0')

app.include_router(todos_router)

@app.on_event('startup')
def on_startup():
    create_db_and_tables()
