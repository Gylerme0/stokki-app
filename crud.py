from sqlalchemy.orm import Session
import models, schemas

# Categoria
def get_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categoria).offset(skip).limit(limit).all()

def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.Categoria(nome=categoria.nome, descricao=categoria.descricao)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria

# Unidade
def get_unidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unidade).offset(skip).limit(limit).all()

def create_unidade(db: Session, unidade: schemas.UnidadeCreate):
    db_unidade = models.Unidade(sigla=unidade.sigla, nome=unidade.nome)
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

# Fornecedor
def get_fornecedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fornecedor).offset(skip).limit(limit).all()

def create_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    db_fornecedor = models.Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

# Endereco
def get_enderecos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Endereco).offset(skip).limit(limit).all()

def create_endereco(db: Session, endereco: schemas.EnderecoCreate):
    db_endereco = models.Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

# Material
def get_materiais(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material
