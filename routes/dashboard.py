from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
