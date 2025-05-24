from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from app.core.app_instance import templates
from app.core.security import get_current_user


html_router = APIRouter(prefix="", tags=["HTML", "Homepage"])

@html_router.get("/", response_class=HTMLResponse)
async def root(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "message": "Use this page to calculate poker odds."
    })