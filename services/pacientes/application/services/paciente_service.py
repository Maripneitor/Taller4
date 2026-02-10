from typing import List, Optional
from services.pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from services.pacientes.application.ports.paciente_repository import PacienteRepository

class PacienteService:
    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def registrar_paciente(self, datos_create: PacienteCreate) -> Paciente:
        datos = {
            "nombre": datos_create.nombre,
            "email": datos_create.email
        }
        return self.repository.save(datos)

    def obtener_paciente(self, id: int) -> Optional[Paciente]:
        return self.repository.find_by_id(id)

    def listar_pacientes(self) -> List[Paciente]:
        return self.repository.find_all()

    def actualizar_paciente(self, id: int, datos_update: PacienteUpdate) -> Optional[Paciente]:
        datos = datos_update.model_dump(exclude_unset=True)
        return self.repository.update(id, datos)

    def eliminar_paciente(self, id: int) -> bool:
        return self.repository.delete(id)
