import os
import django
from django.conf import settings
from django.core.mail import send_mail

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

def test_email():
    try:
        send_mail(
            subject='Portfolio Contact Form Test',
            message='This is a test email from your Django portfolio.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['pokharelbikalsharma@gmail.com'],
            fail_silently=False,
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email failed: {str(e)}")

if __name__ == "__main__":
    test_email()