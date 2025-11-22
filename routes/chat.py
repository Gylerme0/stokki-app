from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/chat")
async def chat_index(request: Request):
    return templates.TemplateResponse("chat/index.html", {"request": request})
