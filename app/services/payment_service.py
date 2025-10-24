from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(**payment.dict(), status="pending")
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_user_payments(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Payment)\
        .join(Payment.property)\
        .filter(Property.owner_id == user_id)\
        .offset(skip)\
        .limit(limit)\
        .all()

def update_payment_status(db: Session, payment_id: int, status: str):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment:
        payment.status = status
        db.commit()
        db.refresh(payment)
    return payment
