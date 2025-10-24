from sqlalchemy.orm import Session
from app.models.property import Property
from app.schemas.property import PropertyCreate, PropertyUpdate
from app.models.user import User

def create_property(db: Session, property: PropertyCreate, current_user: User):
    db_property = Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def get_properties(db: Session, user: User, skip: int = 0, limit: int = 100):
    if user.is_superuser:
        return db.query(Property).offset(skip).limit(limit).all()
    return db.query(Property).filter(Property.owner_id == user.id).offset(skip).limit(limit).all()

def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()
