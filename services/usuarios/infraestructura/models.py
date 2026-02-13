from sqlalchemy import Column, Integer, String
from services.usuarios.infraestructura.database import Base

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    idusuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String, unique=True, index=True)
