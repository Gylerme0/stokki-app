from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/movimentacoes")
async def movimentacoes_index(request: Request):
    return templates.TemplateResponse("movimentacoes/index.html", {"request": request})

@router.get("/movimentacoes/entrada")
async def movimentacoes_entrada(request: Request):
    return templates.TemplateResponse("movimentacoes/entrada.html", {"request": request})

@router.get("/movimentacoes/saida")
async def movimentacoes_saida(request: Request):
    return templates.TemplateResponse("movimentacoes/saida.html", {"request": request})

@router.get("/movimentacoes/transferencia")
async def movimentacoes_transferencia(request: Request):
    return templates.TemplateResponse("movimentacoes/transferencia.html", {"request": request})

@router.get("/movimentacoes/ajuste")
async def movimentacoes_ajuste(request: Request):
    return templates.TemplateResponse("movimentacoes/ajuste.html", {"request": request})
