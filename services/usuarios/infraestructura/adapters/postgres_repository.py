from typing import List, Optional
from sqlalchemy.orm import Session
from services.usuarios.domain.usuario import Usuario
from services.usuarios.application.ports.usuario_repository import UsuarioRepository
from services.usuarios.infraestructura.models import UsuarioDB

class PostgresUsuarioRepository(UsuarioRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, usuario_data: dict) -> Usuario:
        nuevo_usuario_db = UsuarioDB(
            nombre=usuario_data["nombre"],
            email=usuario_data["email"]
        )
        self.db.add(nuevo_usuario_db)
        self.db.commit()
        self.db.refresh(nuevo_usuario_db)
        return self._to_domain(nuevo_usuario_db)

    def find_by_id(self, idusuario: int) -> Optional[Usuario]:
        usuario_db = self.db.query(UsuarioDB).filter(UsuarioDB.idusuario == idusuario).first()
        if usuario_db:
            return self._to_domain(usuario_db)
        return None

    def find_all(self) -> List[Usuario]:
        usuarios_db = self.db.query(UsuarioDB).all()
        return [self._to_domain(u) for u in usuarios_db]

    def update(self, idusuario: int, usuario_data: dict) -> Optional[Usuario]:
        usuario_db = self.db.query(UsuarioDB).filter(UsuarioDB.idusuario == idusuario).first()
        if not usuario_db:
            return None
        
        for key, value in usuario_data.items():
            if value is not None:
                setattr(usuario_db, key, value)
        
        self.db.commit()
        self.db.refresh(usuario_db)
        return self._to_domain(usuario_db)

    def delete(self, idusuario: int) -> bool:
        usuario_db = self.db.query(UsuarioDB).filter(UsuarioDB.idusuario == idusuario).first()
        if usuario_db:
            self.db.delete(usuario_db)
            self.db.commit()
            return True
        return False

    def _to_domain(self, usuario_db: UsuarioDB) -> Usuario:
        return Usuario(
            idusuario=usuario_db.idusuario,
            nombre=usuario_db.nombre,
            email=usuario_db.email
        )
