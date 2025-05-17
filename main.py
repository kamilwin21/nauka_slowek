from fastapi import FastAPI
from database import SessionLocal
from database import engine
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/test")
def read_root():
  return {"message" : "Hello world"}

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/words")
def read_words(db: Session = Depends(get_db)):
  return crud.get_words(db)

@app.post("/words")
def add_word(word: crud.WordCreate, db: Session = Depends(get_db)):
  return crud.create_word(db, word)