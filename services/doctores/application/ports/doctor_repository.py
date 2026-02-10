from abc import ABC, abstractmethod
from typing import List, Optional
from services.doctores.domain.doctor import Doctor

class DoctorRepository(ABC):
    @abstractmethod
    def save(self, datos: dict) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Doctor]:
        pass

    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def update(self, id: int, datos: dict) -> Optional[Doctor]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
