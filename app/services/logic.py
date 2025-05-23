from app.models.poker import PokerRequest, PokerResponse


def calculate_probabilities(request: PokerRequest) -> PokerResponse:
    """
    Simple deterministic calculator:
    - If player has a pair in hand, higher win chance.
    - Otherwise, average probabilities.
    - This is just a stub, no real poker logic yet.
    """
    
    player_hand = request.player_hand
    community_cards = request.community_cards

    # Simplified check: do player cards form a pair?
    ranks = [card[0] for card in player_hand]
    has_pair = ranks[0] == ranks[1]

    if has_pair:
        win = 0.55
        tie = 0.1
        lose = 0.35
    else:
        win = 0.35
        tie = 0.1
        lose = 0.55

    return PokerResponse(
        win_chance=win,
        tie_chance=tie,
        lose_chance=lose
    )
