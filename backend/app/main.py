from fastapi import FastAPI
from routers import users, game
from database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Urubugu Multiplayer Backend",
    version="1.0.0",
    description="REST API for Urubugu Multiplayer Game"
)

# Include routers
app.include_router(users.router, prefix="/auth", tags=["Users"])
app.include_router(game.router, prefix="/game", tags=["Game"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Urubugu Game API!"}

