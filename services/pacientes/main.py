from fastapi import FastAPI
from services.pacientes.infraestructura.api.router import router

app = FastAPI(title="Microservicio de Pacientes", version="1.0.0")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy", "service": "pacientes"}

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
