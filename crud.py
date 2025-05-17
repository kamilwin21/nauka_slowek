from sqlalchemy.orm import Session
from models import Word
from pydantic import BaseModel

class WordCreate(BaseModel):
    english: str
    polish: str

def get_words(db: Session):
    return db.query(Word).all()

def create_word(db: Session, word: WordCreate):
    db_word = Word(english=word.english, polish=word.polish)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word