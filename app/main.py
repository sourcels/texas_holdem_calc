from app.core.app_instance import app
from app.routes import html, service


app.include_router(html.html_router)
app.include_router(service.service_router)