from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/relatorios")
async def relatorios_index(request: Request):
    return templates.TemplateResponse("relatorios/index.html", {"request": request})

@router.get("/relatorios/posicao")
async def relatorios_posicao(request: Request):
    return templates.TemplateResponse("relatorios/posicao.html", {"request": request})

@router.get("/relatorios/rastreabilidade")
async def relatorios_rastreabilidade(request: Request):
    return templates.TemplateResponse("relatorios/rastreabilidade.html", {"request": request})

@router.get("/relatorios/giro")
async def relatorios_giro(request: Request):
    return templates.TemplateResponse("relatorios/giro.html", {"request": request})

@router.get("/relatorios/abc")
async def relatorios_abc(request: Request):
    return templates.TemplateResponse("relatorios/abc.html", {"request": request})
