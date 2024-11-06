from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import User

# Signal to notify Administrators of new user registration
@receiver(post_save, sender=User)
def send_registration_email_to_admin(sender, instance, created, **kwargs):
    if created and instance.approval_status == User.PENDING:
        # Retrieve emails of all Administrator users
        admin_emails = User.objects.filter(role=User.ADMINISTRATOR).values_list('email', flat=True)
        subject = "New User Registration Pending Approval"
        message = (
            f"A new user, {instance.username}, has signed up and requires approval.\n"
            "You can review the registration in the admin dashboard."
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            admin_emails,
            fail_silently=False,
        )

# Signal to notify users upon account activation
@receiver(post_save, sender=User)
def send_activation_email_to_user(sender, instance, **kwargs):
    # Check if user has been approved and profile is still incomplete
    if instance.approval_status == User.APPROVED and not instance.profile_completed:
        subject = "Your Account Has Been Approved"
        message = (
            f"Hi {instance.username},\n\n"
            "Your account has been approved! Please complete your profile by clicking the link below:\n"
            f"{settings.SITE_URL}{reverse('complete_profile')}"
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )
