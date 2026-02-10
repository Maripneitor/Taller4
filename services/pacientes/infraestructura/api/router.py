from fastapi import APIRouter, HTTPException, status
from typing import List
from services.pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from services.pacientes.application.services.paciente_service import PacienteService
from services.pacientes.infraestructura.adapters.in_memory_paciente_repository import InMemoryPacienteRepository

router = APIRouter(prefix="/pacientes", tags=["pacientes"])

repo = InMemoryPacienteRepository()
serv = PacienteService(repo)

@router.post("/", response_model=Paciente, status_code=status.HTTP_201_CREATED)
def crear_paciente(p: PacienteCreate):
    return serv.registrar_paciente(p)

@router.get("/{id}", response_model=Paciente)
def obtener_paciente(id: int):
    p = serv.obtener_paciente(id)
    if p is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return p

@router.get("/", response_model=List[Paciente])
def listar_pacientes():
    return serv.listar_pacientes()

@router.put("/{id}", response_model=Paciente)
def actualizar_paciente(id: int, p: PacienteUpdate):
    pac = serv.actualizar_paciente(id, p)
    if pac is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return pac

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_paciente(id: int):
    fue_eliminado = serv.eliminar_paciente(id)
    if not fue_eliminado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return
