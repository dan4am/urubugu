from sqlalchemy.orm import Session
from models.game import Match, User
from fastapi import HTTPException

class MatchmakingService:
    def __init__(self):
        self.waiting_queue = []  # Temporary in-memory queue for players

    def join_queue(self, player_id: int, db: Session):
        # Check if player is already in a match
        ongoing_match = db.query(Match).filter(
            (Match.player_one == player_id) | (Match.player_two == player_id)
        ).first()

        if ongoing_match:
            raise HTTPException(status_code=400, detail="Player is already in a match")

        # Check if player is already in the queue
        if player_id in self.waiting_queue:
            raise HTTPException(status_code=400, detail="Player is already in the queue")

        # If another player is in the queue, pair them
        if self.waiting_queue:
            opponent_id = self.waiting_queue.pop(0)
            match = Match(player_one=opponent_id, player_two=player_id, game_state={})
            db.add(match)
            db.commit()
            db.refresh(match)
            return {
                "message": "Match created",
                "match_id": match.id,
                "players": [opponent_id, player_id],
            }

        # Otherwise, add the player to the queue
        self.waiting_queue.append(player_id)
        return {"message": "Player added to queue, waiting for an opponent"}

    def leave_queue(self, player_id: int):
        if player_id in self.waiting_queue:
            self.waiting_queue.remove(player_id)
            return {"message": "Player removed from the queue"}
        return {"message": "Player not found in the queue"}

    def complete_match(self, db: Session, match_id):
        def finish_match(self, match_id: int, db: Session):
            # Retrieve the match from the database
            match = db.query(Match).filter(Match.id == match_id).first()

            if not match:
                raise HTTPException(status_code=404, detail="Match not found")

            if match.is_completed:
                raise HTTPException(status_code=400, detail="Match is already completed")

            # Mark the match as completed
            match.is_completed = True
            db.commit()
            return {"message": "Match marked as completed", "match_id": match_id}
    def delete_match(self, match_id: int, db: Session):
        # Retrieve the match from the database
        match = db.query(Match).filter(Match.id == match_id).first()

        if not match:
            raise HTTPException(status_code=404, detail="Match not found")

        # Delete the match
        db.delete(match)
        db.commit()
        return {"message": "Match deleted successfully", "match_id": match_id}

    def get_ongoing_matches(self, db: Session):
        """
        Retrieve all ongoing matches from the database.
        """
        ongoing_matches = db.query(Match).filter(Match.is_completed == False).all()
        return ongoing_matches
