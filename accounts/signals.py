"""
Signal Handlers
This module defines Django signal handlers to manage automated actions related
to user registrations, approvals, disapprovals, and crew bookings.

Signal Functions:
1. notify_admin_of_new_user: Notifies admins of a new user registration.
2. handle_user_status_change: Handles changes in user status and sends
   appropriate emails.
3. adjust_crew_needed: Updates the `crew_needed` count when crew booking
   status changes.
4. increment_crew_needed_on_delete: Adjusts `crew_needed` count when a
   booking is deleted.

Dependencies:
- Django's signals and model event hooks
- Email functionality for notifications
- Models for users, crew bookings, and trips
"""

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import User
from django.apps import apps

# Dynamically import models
CrewBooking = apps.get_model('crewbooking', 'CrewBooking')
Trip = apps.get_model('trips', 'Trip')

# Temporary storage for tracking original status
original_status = {}

@receiver(pre_save, sender=User)
def track_original_status(sender, instance, **kwargs):
    """
    Tracks the original approval status before saving the instance.
    """
    if instance.pk:  # Check if the instance already exists in the database
        original = sender.objects.get(pk=instance.pk)
        original_status[instance.pk] = original.approval_status
    else:
        original_status[instance.pk] = None  # New instance has no original status

@receiver(post_save, sender=User)
def handle_user_status_change(sender, instance, **kwargs):
    """
    Handles changes in user approval status and sends appropriate emails
    for all status changes.
    """
    if getattr(instance, "_skip_signal", False):
        return

    print("Signal received for handle_user_status_change.")

    old_status = original_status.pop(instance.pk, None)
    new_status = instance.approval_status

    print(f"Old status: {old_status}, New status: {new_status}")

    if old_status != new_status:
        print(f"Approval status changed from {old_status} to {new_status}.")

        subject = "Your Account Status Has Changed"
        message = (
            f"Hi {instance.username},\n\n"
            f"Your account status has been updated to: {new_status}.\n\n"
            "Best regards,\n"
            "The CrewFinder Team"
        )

        if new_status == User.APPROVED:
            print("Preparing approval email.")
            instance.is_active = True
            instance._skip_signal = True
            instance.save(update_fields=["is_active"])
            del instance._skip_signal
            subject = "Your Account Has Been Approved"
            try:
                login_url = f"{settings.SITE_URL}{reverse('login')}"
                message = (
                    f"Hi {instance.username},\n\n"
                    "Congratulations! Your account has been approved.\n\n"
                    f"You can log in here: {login_url}\n"
                    f"Once logged in, please complete your profile here: "
                    "Best regards,\n"
                    "The CrewFinder Team"
                )
            except Exception as e:
                print(f"Error resolving URLs: {e}")
                message = (
                    f"Hi {instance.username},\n\n"
                    "Congratulations! Your account has been approved.\n\n"
                    "Please log in to your account and complete your profile.\n\n"
                    "Best regards,\n"
                    "The CrewFinder Team"
                )

        elif new_status == User.DISAPPROVED:
            print("Preparing disapproval email.")
            instance.is_active = False
            instance._skip_signal = True
            instance.save(update_fields=["is_active"])
            del instance._skip_signal
            subject = "Your Account Registration Has Been Disapproved"
            message = (
                f"Hi {instance.username},\n\n"
                "We regret to inform you that your account registration has "
                "been disapproved. Please contact support if you have any "
                "questions.\n\n"
                "Best regards,\n"
                "The CrewFinder Team"
            )

        elif new_status == User.PENDING:
            print("Preparing pending status email.")
            subject = "Your Account Registration is Under Review"
            message = (
                f"Hi {instance.username},\n\n"
                "Your account registration is under review. You will receive "
                "another email once the review process is complete.\n\n"
                "Best regards,\n"
                "The CrewFinder Team"
            )

        from_email = f"CrewFinder Admin <{settings.EMAIL_HOST_USER}>"
        try:
            send_mail(
                subject,
                message,
                from_email,
                [instance.email],
                fail_silently=False,
            )
            print(f"Email sent to {instance.email} about status change to {new_status}.")
        except Exception as e:
            print(f"Error sending email: {e}")

@receiver(post_save, sender=User, dispatch_uid="notify_admin_signal")
def notify_admin_of_new_user(sender, instance, created, **kwargs):
    """
    Sends an email to the admin (EMAIL_HOST_USER) when a new user registers with
    a pending approval status.
    """
    if created and instance.approval_status == User.PENDING:
        print("Signal triggered for notify_admin_of_new_user.")

        admin_email = settings.EMAIL_HOST_USER
        subject = "New User Registration Pending Approval"
        message = (
            f"Hello Admin,\n\n"
            f"A new user has registered on CrewFinder and is awaiting approval. "
            f"Below are the details:\n\n"
            f"Username: {instance.username}\n"
            f"Email: {instance.email}\n\n"
            "To review and approve this registration, please log in to the admin "
            "dashboard.\n\n"
            "Best regards,\n"
            "The CrewFinder Team"
        )
        from_email = f"CrewFinder Admin <{admin_email}>"

        try:
            send_mail(
                subject,
                message,
                from_email,
                [admin_email],
                fail_silently=False,
            )
            print("Admin notification email sent successfully.")
        except Exception as e:
            print(f"Error while sending email: {e}")

@receiver(post_save, sender=CrewBooking)
def adjust_crew_needed(sender, instance, **kwargs):
    """
    Updates the `crew_needed` field of a trip when a crew booking status changes.
    """
    trip = instance.trip

    if instance.status == 'confirmed' and instance._original_status != 'confirmed':
        trip.crew_needed = max(0, trip.crew_needed - 1)
        trip.save()

    elif instance._original_status == 'confirmed' and instance.status != 'confirmed':
        trip.crew_needed += 1
        trip.save()

@receiver(post_delete, sender=CrewBooking)
def increment_crew_needed_on_delete(sender, instance, **kwargs):
    """
    Increments the `crew_needed` field of a trip when a confirmed crew booking is deleted.
    """
    if instance.status == 'confirmed':
        trip = instance.trip
        trip.crew_needed += 1
        trip.save()
