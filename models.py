from database import Base
from sqlalchemy import Column, Integer, Text, TIMESTAMP

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default="now()")