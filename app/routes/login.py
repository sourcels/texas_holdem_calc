from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from app.templates import templates
from app.core.config import settings
from app.services.auth import verify_password, create_token
from app.services.storage import minio_ctrl
from starlette.status import HTTP_302_FOUND


login_router = APIRouter(prefix="/login", tags=["HTML", "SECURITY"])

@login_router.get("", response_class=HTMLResponse)
async def login_page(request: Request):
    next_url = request.query_params.get("next", "/")
    return templates.TemplateResponse("login.html", {
        "request": request,
        "next": next_url
    })

@login_router.post("")
async def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    next: str = Form("/")
):
    if username == "admin" and password == "admin":
        token = create_token(username=username, role="admin")

        response = RedirectResponse(url=next, status_code=302)
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            max_age=settings.jwt_expires_min*60,
            secure=True,
            samesite="lax"
        )
        return response

    return templates.TemplateResponse("login.html", {
        "request": request,
        "next": next,
        "error": "Invalid credentials"
    })