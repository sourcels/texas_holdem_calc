from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from main import app
from models import PokerRequest, PokerResponse
from logic import calculate_probabilities
from config import app

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Use this page to calculate poker odds."})

@app.post(path="/calculate", response_model=PokerResponse)
async def calculate(request: PokerRequest):
    result = calculate_probabilities(request)
    return result