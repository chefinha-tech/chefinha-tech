from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend import models
from backend.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Controle Acadêmico")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API do Controle Acadêmico funcionando!"}
