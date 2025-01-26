from pydantic import BaseModel
class GameMove(BaseModel):
    match_id: int
    player_id: int
    move: dict
