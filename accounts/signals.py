from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import User
from crewbooking.models import CrewBooking
from trips.models import Trip
from django.apps import apps

# Notify administrators of new user registration
@receiver(post_save, sender=User)
def send_registration_email_to_admin(sender, instance, created, **kwargs):
    if instance.approval_status == User.PENDING:
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

# Notify User Of Approval
@receiver(post_save, sender=User)
def send_registration_email_to_admin(sender, instance, created, **kwargs):
        if instance.approval_status == User.APPROVED:
            if not instance.is_active:  # Set to active only if currently inactive
                instance.is_active = True  # Set the user as active
                instance.save(update_fields=['is_active'])  # Save only the `is_active` field
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


# Notify User Of Disapproval
@receiver(post_save, sender=User)
def send_registration_email_to_admin(sender, instance, created, **kwargs):
    if instance.approval_status == User.DISAPPROVED:
            if instance.is_active:  # Set to inactive only if currently active
                instance.is_active = False # Set the user as inactive
                instance.save(update_fields=['is_active'])  # Save only the `is_active` field
            subject = "Your Account Registration Has Been Disapproved"
            message = (
                f"Hi {instance.username},\n\n"
                "We regret to inform you that your account registration has not been approved at this time.\n"
                "Please contact support if you have any questions."
            )
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False,
            )

CrewBooking = apps.get_model('crewbooking', 'CrewBooking')
Trip = apps.get_model('trips', 'Trip')

@receiver(post_save, sender=CrewBooking)
def adjust_crew_needed(sender, instance, **kwargs):
    trip = instance.trip  # Associated trip instance

    # Decrement crew_needed if status changes to 'confirmed'
    if instance.status == 'confirmed' and instance._original_status != 'confirmed':
        trip.crew_needed = max(0, trip.crew_needed - 1)  # Ensure crew_needed is non-negative
        trip.save()

    # Increment crew_needed if the status changes from 'confirmed' to something else
    elif instance._original_status == 'confirmed' and instance.status != 'confirmed':
        trip.crew_needed += 1
        trip.save()