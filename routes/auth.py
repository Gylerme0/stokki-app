from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from config import templates

router = APIRouter()

@router.get("/")
async def read_root(request: Request):
    # In a real app, check auth here
    return RedirectResponse(url="/login")

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    # Mock authentication
    if email and password:
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
