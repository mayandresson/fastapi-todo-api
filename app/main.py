from fastapi import FastAPI
from app.routes.todos import router as todos_router

app = FastAPI(title='To-Do API', version='0.1.0')

# incluir rotas
app.include_router(todos_router)
