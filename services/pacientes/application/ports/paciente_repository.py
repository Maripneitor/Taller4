from abc import ABC, abstractmethod
from typing import List, Optional
from services.pacientes.domain.paciente import Paciente

class PacienteRepository(ABC):
    @abstractmethod
    def save(self, datos: dict) -> Paciente:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Paciente]:
        pass

    @abstractmethod
    def find_all(self) -> List[Paciente]:
        pass

    @abstractmethod
    def update(self, id: int, datos: dict) -> Optional[Paciente]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
