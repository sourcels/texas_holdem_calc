from pydantic import BaseModel
from typing import List


class PokerRequest(BaseModel):
    player_hand: List[str]
    community_cards: List[str]

class PokerResponse(BaseModel):
    win_chance: float
    tie_chance: float
    lose_chance: float