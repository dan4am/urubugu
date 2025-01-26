from sqlalchemy import (Column, Integer, String, ForeignKey,
                        JSON, DateTime, func, Boolean)
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    player_one = Column(Integer, ForeignKey("users.id"), nullable=False)
    player_two = Column(Integer, ForeignKey("users.id"), nullable=True)
    game_state = Column(JSON, default={})
    is_completed = Column(Boolean, default=False)  # Track if the match is completed
    created_at = Column(DateTime, server_default=func.now())
