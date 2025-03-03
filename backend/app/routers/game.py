from fastapi import APIRouter, Depends
from schemas.game_schemas import GameMove
from sqlalchemy.orm import Session

from database import get_db
from models.game import Match
from services.matchmaking import MatchmakingService
from config import config
router = APIRouter()
matchmaking_service = MatchmakingService()


@router.post("/join")
def join_matchmaking(player_id: int , db: Session = Depends(get_db)):
    """
    Player joins the matchmaking queue.
    """
    if player_id == 0:
        player_id = config["user_counter"]
        config["user_counter"] += 1

    print(player_id)
    return matchmaking_service.join_queue(player_id=player_id, db=db)


@router.post("/leave")
def leave_matchmaking(player_id: int):
    """
    Player leaves the matchmaking queue.
    """
    return matchmaking_service.leave_queue(player_id)


@router.get("/get_starting_setting")
def get_starting_setup(player_id: int, db: Session = Depends(get_db)):
    return matchmaking_service.get_other_player_setting(player_id=player_id,
                                                        db=db)


@router.post("/set_starting_setting")
def set_starting_setup(player_id: int,
                       setting: str,
                       db: Session = Depends(get_db)):
    matchmaking_service.set_other_player_setting(player_id=player_id,
                                                 setting=setting,
                                                 db=db)

    return {"result": "new setting set successfully"}


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
