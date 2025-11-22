from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    # In a real app, check auth here
    return RedirectResponse(url="/login")

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    # Mock authentication
    if email and password:
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/movimentacoes")
async def movimentacoes_index(request: Request):
    return templates.TemplateResponse("movimentacoes/index.html", {"request": request})

@app.get("/movimentacoes/entrada")
async def movimentacoes_entrada(request: Request):
    return templates.TemplateResponse("movimentacoes/entrada.html", {"request": request})

@app.get("/movimentacoes/saida")
async def movimentacoes_saida(request: Request):
    return templates.TemplateResponse("movimentacoes/saida.html", {"request": request})

@app.get("/movimentacoes/transferencia")
async def movimentacoes_transferencia(request: Request):
    return templates.TemplateResponse("movimentacoes/transferencia.html", {"request": request})

@app.get("/movimentacoes/ajuste")
async def movimentacoes_ajuste(request: Request):
    return templates.TemplateResponse("movimentacoes/ajuste.html", {"request": request})
