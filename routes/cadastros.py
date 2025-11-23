from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from config import templates
from database import get_db
import crud, schemas

router = APIRouter()

@router.get("/cadastros")
async def cadastros_index(request: Request):
    return templates.TemplateResponse("cadastros/index.html", {"request": request})

@router.get("/cadastros/materiais")
async def cadastros_materiais(request: Request, db: Session = Depends(get_db)):
    materiais = crud.get_materiais(db)
    categorias = crud.get_categorias(db)
    unidades = crud.get_unidades(db)
    return templates.TemplateResponse("cadastros/materiais.html", {
        "request": request, 
        "materiais": materiais,
        "categorias": categorias,
        "unidades": unidades
    })

@router.post("/cadastros/materiais")
async def create_material(
    request: Request,
    sku: str = Form(...),
    descricao: str = Form(...),
    categoria_id: int = Form(...),
    unidade_id: int = Form(...),
    db: Session = Depends(get_db)
):
    material_data = schemas.MaterialCreate(
        sku=sku, 
        descricao=descricao, 
        categoria_id=categoria_id, 
        unidade_id=unidade_id
    )
    crud.create_material(db, material_data)
    return templates.TemplateResponse("cadastros/materiais.html", {
        "request": request, 
        "materiais": crud.get_materiais(db),
        "categorias": crud.get_categorias(db),
        "unidades": crud.get_unidades(db)
    })

@router.get("/cadastros/fornecedores")
async def cadastros_fornecedores(request: Request):
    return templates.TemplateResponse("cadastros/fornecedores.html", {"request": request})

@router.get("/cadastros/enderecos")
async def cadastros_enderecos(request: Request):
    return templates.TemplateResponse("cadastros/enderecos.html", {"request": request})

@router.get("/cadastros/categorias")
async def cadastros_categorias(request: Request, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db)
    return templates.TemplateResponse("cadastros/categorias.html", {"request": request, "categorias": categorias})

@router.post("/cadastros/categorias")
async def create_categoria(request: Request, nome: str = Form(...), descricao: str = Form(None), db: Session = Depends(get_db)):
    categoria_data = schemas.CategoriaCreate(nome=nome, descricao=descricao)
    crud.create_categoria(db, categoria_data)
    categorias = crud.get_categorias(db)
    return templates.TemplateResponse("cadastros/categorias.html", {"request": request, "categorias": categorias})

@router.get("/cadastros/categorias/delete/{id}")
async def delete_categoria(request: Request, id: int, db: Session = Depends(get_db)):
    crud.delete_categoria(db, id)
    categorias = crud.get_categorias(db)
    return templates.TemplateResponse("cadastros/categorias.html", {"request": request, "categorias": categorias})

@router.get("/cadastros/unidades")
async def cadastros_unidades(request: Request, db: Session = Depends(get_db)):
    unidades = crud.get_unidades(db)
    return templates.TemplateResponse("cadastros/unidades.html", {"request": request, "unidades": unidades})

@router.post("/cadastros/unidades")
async def create_unidade(request: Request, sigla: str = Form(...), nome: str = Form(...), db: Session = Depends(get_db)):
    unidade_data = schemas.UnidadeCreate(sigla=sigla, nome=nome)
    crud.create_unidade(db, unidade_data)
    unidades = crud.get_unidades(db)
    return templates.TemplateResponse("cadastros/unidades.html", {"request": request, "unidades": unidades})
