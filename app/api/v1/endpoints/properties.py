from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.base import get_db
from app.schemas.property import Property, PropertyCreate, PropertyUpdate
from app.services import property_service
from app.api.v1.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=Property)
def create_property(
    property: PropertyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return property_service.create_property(db, property, current_user)

@router.get("/", response_model=List[Property])
def read_properties(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return property_service.get_properties(db, current_user, skip, limit)

@router.get("/{property_id}", response_model=Property)
def read_property(
    property_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    property = property_service.get_property(db, property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    if property.owner_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return property
