from pydantic import BaseModel
from typing import Optional, List

# Categoria
class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    class Config:
        orm_mode = True

# Unidade
class UnidadeBase(BaseModel):
    sigla: str
    nome: str

class UnidadeCreate(UnidadeBase):
    pass

class Unidade(UnidadeBase):
    id: int
    class Config:
        orm_mode = True

# Fornecedor
class FornecedorBase(BaseModel):
    nome: str
    cnpj: str
    contato: Optional[str] = None

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int
    class Config:
        orm_mode = True

# Endereco
class EnderecoBase(BaseModel):
    codigo: str
    descricao: Optional[str] = None

class EnderecoCreate(EnderecoBase):
    pass

class Endereco(EnderecoBase):
    id: int
    class Config:
        orm_mode = True

# Material
class MaterialBase(BaseModel):
    sku: str
    descricao: str
    categoria_id: int
    unidade_id: int
    estoque_atual: Optional[float] = 0.0
    fornecedor_padrao_id: Optional[int] = None
    endereco_picking_id: Optional[int] = None

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int
    class Config:
        orm_mode = True

# Usuario
class UsuarioBase(BaseModel):
    username: str
    email: str
    role: str = "user"

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
