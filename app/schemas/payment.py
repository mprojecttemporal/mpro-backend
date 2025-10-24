from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    amount: float
    method: str
    property_id: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    status: str
    date: datetime

    class Config:
        orm_mode = True
