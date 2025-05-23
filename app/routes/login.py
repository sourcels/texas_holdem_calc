from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from app.services.auth import verify_password, create_token
from app.services.storage import get_users
from starlette.status import HTTP_302_FOUND


login_router = APIRouter(prefix="/login", tags=["API"])

@login_router.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    redirect: str = Form(default="/")
):
    users = get_users()
    user = users.get(username)

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": username, "role": user["role"]})
    
    response = RedirectResponse(url=redirect, status_code=HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    return response