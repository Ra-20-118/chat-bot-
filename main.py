from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Message
from pydantic import BaseModel  # BaseModel


Base.metadata.create_all(bind=engine)

app = FastAPI()


class MessageRequest(BaseModel):
    user_input: str
    bot_response: str
    
    #اdatabase session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 
@app.post("/messages/")
def create_message(message: MessageRequest, db: Session = Depends(get_db)):
    new_message = Message(user_input=message.user_input, bot_response=message.bot_response)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

#  
@app.get("/messages/")
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()



