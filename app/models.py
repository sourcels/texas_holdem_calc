from pydantic import BaseModel
from typing import List, Callable
from starlette.types import ASGIApp


class Config(BaseModel):
    app: ASGIApp
    host: str
    port: int
    reload: str
    log_level: str
    workers: int

class PokerRequest(BaseModel):
    player_hand: List[str]
    community_cards: List[str]

class PokerResponse(BaseModel):
    win_chance: float
    tie_chance: float
    lose_chance: float