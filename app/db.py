from typing import Generator
import os
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./dev.db')

# se sqlite usar check_same_thread
connect_args = {}
if DATABASE_URL.startswith('sqlite'):
    connect_args = {"connect_args": {"check_same_thread": False}}

engine = create_engine(DATABASE_URL, echo=False, **(connect_args or {}))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
