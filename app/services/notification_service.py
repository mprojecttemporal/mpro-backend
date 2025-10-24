from typing import Dict, Any

class NotificationService:
    @staticmethod
    def send_payment_notification(user_email: str, payment_data: Dict[str, Any]):
        print(f"[EMAIL] Payment notification sent to {user_email}")
        print(f"Payment details: {payment_data}")
    
    @staticmethod
    def send_registration_notification(email: str):
        print(f"[EMAIL] Welcome email sent to {email}")

notification_service = NotificationService()
