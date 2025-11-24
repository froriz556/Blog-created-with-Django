from random import randint
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailCodeVerification

def send_code(user):

    code = str(randint(100000, 999999))

    EmailCodeVerification.objects.create(
        user=user,
        code=code,
        end_time=timezone.now() + timedelta(minutes=5)
    )

    print(f"\n====== CODE FOR {user.email} ======")
    print(f"Verification code: {code}")
    print("=================================\n")

    subject = "Подтверждение вашей электронной почты"
    message = f"Ваш код подтверждения: {code}. Он действителен 5 минут."

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
    print(code)
    return code
