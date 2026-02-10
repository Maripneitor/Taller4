from typing import List, Optional
from services.doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from services.doctores.application.ports.doctor_repository import DoctorRepository

class DoctorService:
    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def registrar_doctor(self, datos_create: DoctorCreate) -> Doctor:
        datos = {
            "nombre": datos_create.nombre,
            "especialidad": datos_create.especialidad
        }
        return self.repository.save(datos)

    def obtener_doctor(self, id: int) -> Optional[Doctor]:
        return self.repository.find_by_id(id)

    def listar_doctores(self) -> List[Doctor]:
        return self.repository.find_all()

    def actualizar_doctor(self, id: int, datos_update: DoctorUpdate) -> Optional[Doctor]:
        datos = datos_update.model_dump(exclude_unset=True)
        return self.repository.update(id, datos)

    def eliminar_doctor(self, id: int) -> bool:
        return self.repository.delete(id)
