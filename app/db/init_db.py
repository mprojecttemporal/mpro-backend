from sqlalchemy.orm import Session
from app.db.base import Base, engine
from app.core.config import settings
from app.services import user_service
from app.schemas.user import UserCreate

def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    
    # Crear superusuario si no existe
    user = user_service.get_user_by_email(db, settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name="Initial Admin",
            is_superuser=True
        )
        user_service.create_user(db, user_in)

if __name__ == "__main__":
    from app.db.base import SessionLocal
    db = SessionLocal()
    init_db(db)
