from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String)

    materiais = relationship("Material", back_populates="categoria")

class Unidade(Base):
    __tablename__ = "unidades"

    id = Column(Integer, primary_key=True, index=True)
    sigla = Column(String, unique=True, index=True)
    nome = Column(String)

    materiais = relationship("Material", back_populates="unidade")

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    contato = Column(String)
    
    materiais = relationship("Material", back_populates="fornecedor_padrao")

class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True) # Ex: 01-A-01
    descricao = Column(String)

    materiais = relationship("Material", back_populates="endereco_picking")

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    descricao = Column(String, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    unidade_id = Column(Integer, ForeignKey("unidades.id"))
    estoque_atual = Column(Float, default=0.0)
    fornecedor_padrao_id = Column(Integer, ForeignKey("fornecedores.id"), nullable=True)
    endereco_picking_id = Column(Integer, ForeignKey("enderecos.id"), nullable=True)

    categoria = relationship("Categoria", back_populates="materiais")
    unidade = relationship("Unidade", back_populates="materiais")
    fornecedor_padrao = relationship("Fornecedor", back_populates="materiais")
    endereco_picking = relationship("Endereco", back_populates="materiais")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user") # admin, user

class Auditoria(Base):
    __tablename__ = "auditoria"

    id = Column(Integer, primary_key=True, index=True)
    acao = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    data_hora = Column(DateTime, default=datetime.utcnow)
    detalhes = Column(String)

    usuario = relationship("Usuario")
