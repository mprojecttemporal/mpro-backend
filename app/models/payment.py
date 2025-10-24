from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    status = Column(String)  # pending, completed, failed
    method = Column(String)  # credit_card, cash, transfer
    date = Column(DateTime, default=datetime.utcnow)
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="payments")
