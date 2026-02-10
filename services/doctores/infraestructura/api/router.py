from fastapi import APIRouter, HTTPException, status
from typing import List
from services.doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from services.doctores.application.services.doctor_service import DoctorService
from services.doctores.infraestructura.adapters.in_memory_doctor_repository import InMemoryDoctorRepository

router = APIRouter(prefix="/doctores", tags=["doctores"])

repo = InMemoryDoctorRepository()
serv = DoctorService(repo)

@router.post("/", response_model=Doctor, status_code=status.HTTP_201_CREATED)
def crear_doctor(d: DoctorCreate):
    return serv.registrar_doctor(d)

@router.get("/{id}", response_model=Doctor)
def obtener_doctor(id: int):
    d = serv.obtener_doctor(id)
    if d is None:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return d

@router.get("/", response_model=List[Doctor])
def listar_doctores():
    return serv.listar_doctores()

@router.put("/{id}", response_model=Doctor)
def actualizar_doctor(id: int, d: DoctorUpdate):
    doc = serv.actualizar_doctor(id, d)
    if doc is None:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doc

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_doctor(id: int):
    fue_eliminado = serv.eliminar_doctor(id)
    if not fue_eliminado:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return
