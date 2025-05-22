from fastapi import FastAPI
from app.models import PokerRequest, PokerResponse
from app.logic import calculate_probabilities

app = FastAPI(title="Texas Hold'em Calculator")

@app.post(path="/calculate", response_model=PokerResponse)
async def calculate(request: PokerRequest):
    result = calculate_probabilities(request)
    return result

