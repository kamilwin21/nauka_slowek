from fastapi import FastAPI
# from database import SessionLocal
# import models

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/test")
def read_root():
  return {"message" : "Hello world"}

# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()
