from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.core.app_instance import templates


html_router = APIRouter(prefix="", tags=["HTML"])

@html_router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "message": "Use this page to calculate poker odds."
    })