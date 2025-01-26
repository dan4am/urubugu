from fastapi import APIRouter, Depends
from schemas.game_schemas import GameMove
from sqlalchemy.orm import Session

from database import get_db
from models.game import Match
from services.matchmaking import MatchmakingService

router = APIRouter()
matchmaking_service = MatchmakingService()


@router.post("/join")
def join_matchmaking(player_id: int, db: Session = Depends(get_db)):
    """
    Player joins the matchmaking queue.
    """
    return matchmaking_service.join_queue(player_id, db)

@router.post("/leave")
def leave_matchmaking(player_id: int):
    """
    Player leaves the matchmaking queue.
    """
    return matchmaking_service.leave_queue(player_id)


# @app.post("/game/move")
# def submit_move(game_id: str, player_id: str, move: dict):
#     # Update the game state with the player's move
#     return {"status": "move received", "game_id": game_id}

@router.post("/move")
def make_move(move: GameMove, db: Session = Depends(get_db)):
    match = db.query(Match).filter(Match.id == move.match_id).first()
    if not match:
        return {"error": "Match not found"}
    # Update game state logic here
    return {"message": "Move accepted", "new_state": match.game_state}

@router.post("/finish")
def finish_match(match_id: int, db: Session = Depends(get_db)):
    """
    Mark a match as completed.
    """
    return matchmaking_service.complete_match(match_id, db)

@router.delete("/delete")
def delete_match(match_id: int, db: Session = Depends(get_db)):
    """
    Delete a match from the database.
    """
    return matchmaking_service.delete_match(match_id, db)

@router.get("/ongoing")
def get_ongoing_matches(db: Session = Depends(get_db)):
    """
    Get all ongoing matches.
    """
    matches = matchmaking_service.get_ongoing_matches(db)
    return {"ongoing_matches": matches}