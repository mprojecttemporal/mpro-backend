from pydantic import BaseModel

class PropertyBase(BaseModel):
    name: str
    address: str
    tower: str | None = None
    apartment_number: str

class PropertyCreate(PropertyBase):
    owner_id: int

class PropertyUpdate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
