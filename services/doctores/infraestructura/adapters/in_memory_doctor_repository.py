from typing import List, Optional, Dict
from services.doctores.domain.doctor import Doctor
from services.doctores.application.ports.doctor_repository import DoctorRepository

class InMemoryDoctorRepository(DoctorRepository):
    def __init__(self):
        self.doctores: Dict[int, Doctor] = {}
        self.proximo_id = 1

    def save(self, datos: dict) -> Doctor:
        nuevo_doctor = Doctor(
            id=self.proximo_id,
            nombre=datos["nombre"],
            especialidad=datos["especialidad"]
        )
        self.doctores[self.proximo_id] = nuevo_doctor
        self.proximo_id = self.proximo_id + 1
        return nuevo_doctor

    def find_by_id(self, id: int) -> Optional[Doctor]:
        if id in self.doctores:
            return self.doctores[id]
        return None

    def find_all(self) -> List[Doctor]:
        lista = []
        for p in self.doctores.values():
            lista.append(p)
        return lista

    def update(self, id: int, datos: dict) -> Optional[Doctor]:
        if id not in self.doctores:
            return None
        
        actual = self.doctores[id]
        nuevo = actual.model_copy(update=datos)
        self.doctores[id] = nuevo
        return nuevo

    def delete(self, id: int) -> bool:
        if id in self.doctores:
            del self.doctores[id]
            return True
        return False
