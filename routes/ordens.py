from fastapi import APIRouter, Request
from config import templates

router = APIRouter()

@router.get("/ordens")
async def ordens_index(request: Request):
    return templates.TemplateResponse("ordens/index.html", {"request": request})

@router.get("/ordens/monitor")
async def ordens_monitor(request: Request):
    return templates.TemplateResponse("ordens/monitor.html", {"request": request})

@router.get("/ordens/criar")
async def ordens_criar(request: Request):
    return templates.TemplateResponse("ordens/criar.html", {"request": request})

@router.get("/ordens/lista/{id}")
async def ordens_lista(request: Request, id: str):
    return templates.TemplateResponse("ordens/lista.html", {"request": request, "id": id})
