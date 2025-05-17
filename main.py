from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
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

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
  total = db.query(Word).count()
  today = datetime.utcnow().date()
  last_week = today - timedelta(days=7)

  last7 = db.query(Word).filter(Word.created_at >= last_week).count()
  return {
    "total_words":total,
    "added_last_7_days":last7,
  }
