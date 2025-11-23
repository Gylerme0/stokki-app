from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import auth, dashboard, movimentacoes, ordens, relatorios, cadastros, administracao, chat
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Routers
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(movimentacoes.router)
app.include_router(ordens.router)
app.include_router(relatorios.router)
app.include_router(cadastros.router)
app.include_router(administracao.router)
app.include_router(chat.router)
