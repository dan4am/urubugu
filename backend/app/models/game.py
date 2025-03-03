from sqlalchemy import (Column, Integer, String, ForeignKey,
                        JSON, DateTime, func, Boolean)
from database import Base

default_setting = "2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2"
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
    player_one_starting_setting = Column(String, nullable=True, default=default_setting)
    player_two_starting_setting = Column(String, nullable=True, default=default_setting)
    player_one_moves = Column(JSON, default={})
    player_two_moves = Column(JSON, default={})
    game_state = Column(JSON, default={})
    is_completed = Column(Boolean, default=False)  # Track if the match is completed
    created_at = Column(DateTime, server_default=func.now())
