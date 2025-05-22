from pydantic import BaseModel
from typing import List

class PokerRequest(BaseModel):
    player_hand: List[str]  # ['As', 'Kd']
    community_cards: List[str]  # ['2c', '5d', 'Jh']

class PokerResponse(BaseModel):
    win_chance: float
    tie_chance: float
    lose_chance: float