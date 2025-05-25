from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.routes import html, login, service


app = FastAPI(title="Poker Probality Calculator")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.middleware("http")
async def redirect_unauthenticated_users(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 401:
        return RedirectResponse(url=f"/login?next={request.url.path}")
    return response

app.include_router(html.html_router)
app.include_router(login.login_router)
app.include_router(service.service_router)