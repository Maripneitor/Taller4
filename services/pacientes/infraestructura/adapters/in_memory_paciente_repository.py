from typing import List, Optional, Dict
from services.pacientes.domain.paciente import Paciente
from services.pacientes.application.ports.paciente_repository import PacienteRepository

class InMemoryPacienteRepository(PacienteRepository):
    def __init__(self):
        self.pacientes: Dict[int, Paciente] = {}
        self.proximo_id = 1

    def save(self, paciente_data: dict) -> Paciente:
        nuevo_paciente = Paciente(
            id=self.proximo_id,
            nombre=paciente_data["nombre"],
            email=paciente_data["email"]
        )
        self.pacientes[self.proximo_id] = nuevo_paciente
        self.proximo_id = self.proximo_id + 1
        return nuevo_paciente

    def find_by_id(self, id: int) -> Optional[Paciente]:
        if id in self.pacientes:
            return self.pacientes[id]
        return None

    def find_all(self) -> List[Paciente]:
        lista = []
        for p in self.pacientes.values():
            lista.append(p)
        return lista

    def update(self, id: int, paciente_data: dict) -> Optional[Paciente]:
        if id not in self.pacientes:
            return None
        
        paciente_actual = self.pacientes[id]
        paciente_actualizado = paciente_actual.model_copy(update=paciente_data)
        self.pacientes[id] = paciente_actualizado
        return paciente_actualizado

    def delete(self, id: int) -> bool:
        if id in self.pacientes:
            del self.pacientes[id]
            return True
        return False
