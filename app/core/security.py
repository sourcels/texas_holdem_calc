from fastapi import Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.models.user import TokenData
from app.core.config import settings

security = HTTPBearer(auto_error=False)

def get_current_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(url=f"/login?next={request.url.path}")

    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        return TokenData(**payload)
    except JWTError:
        return RedirectResponse(url=f"/login?next={request.url.path}")

def require_role(role: str):
    def role_dependency(user: TokenData = Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient privileges")
        return user
    return role_dependency
