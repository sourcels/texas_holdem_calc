from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from app.templates import templates
from app.models.user import TokenData
from app.core.security import get_current_user


html_router = APIRouter(prefix="", tags=["HTML", "Homepage"])

@html_router.get("/", response_class=HTMLResponse)
async def root(request: Request, user: TokenData=Depends(get_current_user)):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "message": "Use this page to calculate poker odds."
    })