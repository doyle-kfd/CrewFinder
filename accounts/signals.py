"""
Signal Handlers
This module defines Django signal handlers to manage automated actions related
to user registrations, approvals, disapprovals, and crew bookings.

Signal Functions:
1. track_original_status: Tracks the original approval status of a user.
2. handle_user_status_change: Sends emails based on changes in user status.
3. notify_admin_of_new_user: Notifies admins of a new user registration.
4. adjust_crew_needed: Updates the `crew_needed` count for trip bookings.
5. increment_crew_needed_on_delete: Adjusts `crew_needed` when a booking is
   deleted.

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
from django.apps import apps
from .models import User

# Dynamically import models
CrewBooking = apps.get_model('crewbooking', 'CrewBooking')
Trip = apps.get_model('trips', 'Trip')

# Temporary storage for tracking original status
original_status = {}


@receiver(pre_save, sender=User)
def track_original_status(sender, instance, **kwargs):
    """
    Track the original approval status of a User instance before saving.

    Args:
        sender (Model): The User model.
        instance (User): The user instance being saved.
    """
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)
        original_status[instance.pk] = original.approval_status
    else:
        original_status[instance.pk] = None


@receiver(post_save, sender=User)
def handle_user_status_change(sender, instance, **kwargs):
    """
    Send emails to users when their approval status changes.

    Updates account activation status based on the new approval status.

    Args:
        sender (Model): The User model.
        instance (User): The user instance being saved.
    """
    if getattr(instance, "_skip_signal", False):
        return

    old_status = original_status.pop(instance.pk, None)
    new_status = instance.approval_status

    if old_status == new_status:
        return

    from_email = f"CrewFinder Admin <{settings.EMAIL_HOST_USER}>"

    if new_status == User.APPROVED:
        instance.is_active = True
        instance._skip_signal = True
        instance.save(update_fields=["is_active"])
        del instance._skip_signal

        subject = "Your Account Has Been Approved yes"
        complete_url = f"{settings.SITE_URL}{reverse('accounts:complete_profile')}"
        message = (
            f"Hi {instance.username},\n\n"
            "Your account has been approved.\n\n"
            f"Complete your profile here: {complete_url}\n\n"
            "Best regards,\nCrewFinder Team"
        )

    elif new_status == User.DISAPPROVED:
        instance.is_active = False
        instance._skip_signal = True
        instance.save(update_fields=["is_active"])
        del instance._skip_signal

        subject = "Your Account Registration Has Been Disapproved"
        message = (
            f"Hi {instance.username},\n\n"
            "Unfortunately, your account registration has been disapproved.\n"
            "Please contact support for further assistance.\n\n"
            "Best regards,\nCrewFinder Team"
        )

    elif new_status == User.PENDING:
        subject = "Your Account Registration is Under Review"
        message = (
            f"Hi {instance.username},\n\n"
            "Your account registration is under review.\n"
            "You will receive another email when the process is complete.\n\n"
            "Best regards,\nCrewFinder Team"
        )

    else:
        return

    send_mail(
        subject,
        message,
        from_email,
        [instance.email],
        fail_silently=False,
    )


@receiver(post_save, sender=User, dispatch_uid="notify_admin_signal")
def notify_admin_of_new_user(sender, instance, created, **kwargs):
    """
    Notify the admin when a new user registers with pending approval status.

    Args:
        sender (Model): The User model.
        instance (User): The newly created user instance.
        created (bool): Indicates if the instance is newly created.
    """
    if created and instance.approval_status == User.PENDING:
        admin_email = settings.EMAIL_HOST_USER
        subject = "New User Registration Pending Approval"
        message = (
            f"Hello Admin,\n\n"
            f"A new user has registered:\n\n"
            f"Username: {instance.username}\n"
            f"Email: {instance.email}\n\n"
            "Please log in to the admin dashboard to review and approve.\n\n"
            "Best regards,\nCrewFinder Team"
        )

        send_mail(
            subject,
            message,
            admin_email,
            [admin_email],
            fail_silently=False,
        )


@receiver(post_save, sender=CrewBooking)
def adjust_crew_needed(sender, instance, **kwargs):
    """
    Adjust the `crew_needed` count for a trip when a crew booking's status
    changes.

    Args:
        sender (Model): The CrewBooking model.
        instance (CrewBooking): The booking instance being saved.
    """
    trip = instance.trip

    if (instance.status == 'confirmed' and
            instance._original_status != 'confirmed'):
        trip.crew_needed = max(0, trip.crew_needed - 1)
        trip.save()

    elif (instance._original_status == 'confirmed' and
          instance.status != 'confirmed'):
        trip.crew_needed += 1
        trip.save()


@receiver(post_delete, sender=CrewBooking)
def increment_crew_needed_on_delete(sender, instance, **kwargs):
    """
    Increment the `crew_needed` count when a confirmed crew booking is deleted.

    Args:
        sender (Model): The CrewBooking model.
        instance (CrewBooking): The booking instance being deleted.
    """
    if instance.status == 'confirmed':
        trip = instance.trip
        trip.crew_needed += 1
        trip.save()
