from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/cadastros")
async def cadastros_index(request: Request):
    return templates.TemplateResponse("cadastros/index.html", {"request": request})

@router.get("/cadastros/materiais")
async def cadastros_materiais(request: Request):
    return templates.TemplateResponse("cadastros/materiais.html", {"request": request})

@router.get("/cadastros/fornecedores")
async def cadastros_fornecedores(request: Request):
    return templates.TemplateResponse("cadastros/fornecedores.html", {"request": request})

@router.get("/cadastros/enderecos")
async def cadastros_enderecos(request: Request):
    return templates.TemplateResponse("cadastros/enderecos.html", {"request": request})

@router.get("/cadastros/categorias")
async def cadastros_categorias(request: Request):
    return templates.TemplateResponse("cadastros/categorias.html", {"request": request})

@router.get("/cadastros/unidades")
async def cadastros_unidades(request: Request):
    return templates.TemplateResponse("cadastros/unidades.html", {"request": request})
