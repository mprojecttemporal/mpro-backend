from fastapi import FastAPI
from app.api.v1.endpoints import users, auth, properties

app = FastAPI(title="Property Manager API")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(properties.router, prefix="/api/v1/properties", tags=["Properties"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
