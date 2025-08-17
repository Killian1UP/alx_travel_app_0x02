from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(user_email, booking_id):
    send_mail(
        subject="Booking Payment Confirmed",
        message=f"Your booking {booking_id} has been successfully paid.",
        from_email="noreply@example.com",
        recipient_list=[user_email]
    )
