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

@app.get("/ordens")
async def ordens_index(request: Request):
    return templates.TemplateResponse("ordens/index.html", {"request": request})

@app.get("/ordens/monitor")
async def ordens_monitor(request: Request):
    return templates.TemplateResponse("ordens/monitor.html", {"request": request})

@app.get("/ordens/criar")
async def ordens_criar(request: Request):
    return templates.TemplateResponse("ordens/criar.html", {"request": request})

@app.get("/ordens/lista/{id}")
async def ordens_lista(request: Request, id: str):
    return templates.TemplateResponse("ordens/lista.html", {"request": request, "id": id})

@app.get("/relatorios")
async def relatorios_index(request: Request):
    return templates.TemplateResponse("relatorios/index.html", {"request": request})

@app.get("/relatorios/posicao")
async def relatorios_posicao(request: Request):
    return templates.TemplateResponse("relatorios/posicao.html", {"request": request})

@app.get("/relatorios/rastreabilidade")
async def relatorios_rastreabilidade(request: Request):
    return templates.TemplateResponse("relatorios/rastreabilidade.html", {"request": request})

@app.get("/relatorios/giro")
async def relatorios_giro(request: Request):
    return templates.TemplateResponse("relatorios/giro.html", {"request": request})

@app.get("/relatorios/abc")
async def relatorios_abc(request: Request):
    return templates.TemplateResponse("relatorios/abc.html", {"request": request})

@app.get("/cadastros")
async def cadastros_index(request: Request):
    return templates.TemplateResponse("cadastros/index.html", {"request": request})

@app.get("/cadastros/materiais")
async def cadastros_materiais(request: Request):
    return templates.TemplateResponse("cadastros/materiais.html", {"request": request})

@app.get("/cadastros/fornecedores")
async def cadastros_fornecedores(request: Request):
    return templates.TemplateResponse("cadastros/fornecedores.html", {"request": request})

@app.get("/cadastros/enderecos")
async def cadastros_enderecos(request: Request):
    return templates.TemplateResponse("cadastros/enderecos.html", {"request": request})

@app.get("/cadastros/categorias")
async def cadastros_categorias(request: Request):
    return templates.TemplateResponse("cadastros/categorias.html", {"request": request})

@app.get("/cadastros/unidades")
async def cadastros_unidades(request: Request):
    return templates.TemplateResponse("cadastros/unidades.html", {"request": request})

@app.get("/administracao")
async def administracao_index(request: Request):
    return templates.TemplateResponse("administracao/index.html", {"request": request})

@app.get("/administracao/usuarios")
async def administracao_usuarios(request: Request):
    return templates.TemplateResponse("administracao/usuarios.html", {"request": request})

@app.get("/administracao/auditoria")
async def administracao_auditoria(request: Request):
    return templates.TemplateResponse("administracao/auditoria.html", {"request": request})

@app.get("/chat")
async def chat_index(request: Request):
    return templates.TemplateResponse("chat/index.html", {"request": request})
