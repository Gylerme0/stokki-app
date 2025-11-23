from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from config import templates
from database import get_db
import crud, schemas

router = APIRouter()

@router.get("/administracao")
async def administracao_index(request: Request):
    return templates.TemplateResponse("administracao/index.html", {"request": request})

@router.get("/administracao/usuarios")
async def administracao_usuarios(request: Request, db: Session = Depends(get_db)):
    usuarios = db.query(crud.models.Usuario).all()
    return templates.TemplateResponse("administracao/usuarios.html", {"request": request, "usuarios": usuarios})

@router.post("/administracao/usuarios")
async def create_usuario(
    request: Request, 
    username: str = Form(...), 
    email: str = Form(...), 
    password: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    # Hash password logic should be here, but for simplicity we store plain text or simple hash
    # In a real app, use bcrypt
    usuario_data = schemas.UsuarioCreate(username=username, email=email, password=password, role=role)
    db_usuario = crud.models.Usuario(
        username=usuario_data.username, 
        email=usuario_data.email, 
        hashed_password=usuario_data.password, # TODO: Hash this
        role=usuario_data.role
    )
    db.add(db_usuario)
    db.commit()
    
    usuarios = db.query(crud.models.Usuario).all()
    return templates.TemplateResponse("administracao/usuarios.html", {"request": request, "usuarios": usuarios})

@router.get("/administracao/auditoria")
async def administracao_auditoria(request: Request):
    return templates.TemplateResponse("administracao/auditoria.html", {"request": request})
