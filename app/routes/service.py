from fastapi import APIRouter
from app.models.poker import PokerResponse, PokerRequest
from app.services.logic import calculate_probabilities


service_router = APIRouter(prefix="/api", tags=["API"])

@service_router.post(path="/calculate", response_model=PokerResponse)
async def calculate(request: PokerRequest):
    result = calculate_probabilities(request)
    return result