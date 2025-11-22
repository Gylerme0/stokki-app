from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/administracao")
async def administracao_index(request: Request):
    return templates.TemplateResponse("administracao/index.html", {"request": request})

@router.get("/administracao/usuarios")
async def administracao_usuarios(request: Request):
    return templates.TemplateResponse("administracao/usuarios.html", {"request": request})

@router.get("/administracao/auditoria")
async def administracao_auditoria(request: Request):
    return templates.TemplateResponse("administracao/auditoria.html", {"request": request})
