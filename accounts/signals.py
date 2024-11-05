from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import User

@receiver(post_save, sender=User)
def send_registration_email_to_admin(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        admin_emails = User.objects.filter(role=User.ADMINISTRATOR).values_list('email', flat=True)
        subject = "New User Registration Pending Approval"
        message = f"A new user, {instance.username}, has signed up and requires approval. You can review the registration in the admin dashboard."
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            admin_emails,
            fail_silently=False,
        )

@receiver(post_save, sender=User)
def send_activation_email_to_user(sender, instance, **kwargs):
    if instance.is_active and not instance.profile_completed:
        subject = "Your Account Has Been Approved"
        message = f"Hi {instance.username},\n\nYour account has been approved! Please complete your profile by clicking the link below:\n{settings.SITE_URL}{reverse('complete_profile')}"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )