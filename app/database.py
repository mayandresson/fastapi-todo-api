from sqlmodel import create_engine, SQLModel, Session
from app.core.config import DATABASE_URL

# detect sqlite to set connect_args
connect_args = {}
if DATABASE_URL.startswith('sqlite'):
    connect_args = { 'connect_args': {'check_same_thread': False} }

engine = create_engine(DATABASE_URL, echo=False, **(connect_args or {}))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
