"""
Signal Handlers
This module defines Django signal handlers to manage automated
actions related to
user registrations, approvals, disapprovals, and crew bookings.

Signal Functions:
1. notify_admin_of_new_user: Notifies admins of a new user registration.
2. notify_user_of_approval: Activates a user's account and sends an
   approval email.
3. notify_user_of_disapproval: Deactivates a user's account and sends
   a disapproval email.
4. adjust_crew_needed: Updates the `crew_needed` count when crew booking
   status changes.
5. increment_crew_needed_on_delete: Adjusts `crew_needed` count when a
   booking is deleted.

Dependencies:
- Django's signals and model event hooks
- Email functionality for notifications
- Models for users, crew bookings, and trips
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import User
from django.apps import apps

# Dynamically import models
CrewBooking = apps.get_model('crewbooking', 'CrewBooking')
Trip = apps.get_model('trips', 'Trip')


@receiver(post_save, sender=User)
def notify_admin_of_new_user(sender, instance, created, **kwargs):
    """
    Sends an email to administrators when a new user registers with a
    pending approval status.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (User): The instance of the user that was created or saved.
        created (bool): Indicates if the instance was created.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    if instance.approval_status == User.PENDING:
        admin_emails = User.objects.filter(
            role=User.ADMINISTRATOR
        ).values_list('email', flat=True)

        subject = "New User Registration Pending Approval"
        message = (
            f"A new user, {instance.username}, has signed up and requires "
            "approval.\nYou can review the registration in the admin "
            "dashboard."
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            admin_emails,
            fail_silently=False,
        )


@receiver(post_save, sender=User)
def notify_user_of_approval(sender, instance, created, **kwargs):
    """
    Activates a user account and sends an approval email when their
    registration is approved.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (User): The instance of the user that was updated.
        created (bool): Indicates if the instance was created.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    if instance.approval_status == User.APPROVED and not instance.is_active:
        instance.is_active = True
        instance.save(update_fields=['is_active'])  # Save only `is_active`

        subject = "Your Account Has Been Approved"
        message = (
            f"Hi {instance.username},\n\nYour account has been approved! "
            "Please complete your profile by clicking the link below:\n"
            f"{settings.SITE_URL}{reverse('complete_profile')}"
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )


@receiver(post_save, sender=User)
def notify_user_of_disapproval(sender, instance, created, **kwargs):
    """
    Deactivates a user account and sends a disapproval email if the
    registration is disapproved.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (User): The instance of the user that was updated.
        created (bool): Indicates if the instance was created.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    if instance.approval_status == User.DISAPPROVED and instance.is_active:
        instance.is_active = False
        instance.save(update_fields=['is_active'])  # Save only `is_active`

        subject = "Your Account Registration Has Been Disapproved"
        message = (
            f"Hi {instance.username},\n\nWe regret to inform you that your "
            "account registration has not been approved at this time.\n"
            "Please contact support if you have any questions."
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )


@receiver(post_save, sender=CrewBooking)
def adjust_crew_needed(sender, instance, **kwargs):
    """
    Updates the `crew_needed` field of a trip when a crew booking status
    changes.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (CrewBooking): The instance of the booking that was updated.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    trip = instance.trip

    if (instance.status ==
            'confirmed' and instance._original_status != 'confirmed'):
        trip.crew_needed = max(0, trip.crew_needed - 1)  # Prevent negative
        trip.save()

    elif (instance._original_status ==
          'confirmed' and instance.status != 'confirmed'):
        trip.crew_needed += 1
        trip.save()


@receiver(post_delete, sender=CrewBooking)
def increment_crew_needed_on_delete(sender, instance, **kwargs):
    """
    Increments the `crew_needed` field of a trip when a confirmed crew
    booking is deleted.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (CrewBooking): The instance of the booking that was deleted.
        kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    if instance.status == 'confirmed':
        trip = instance.trip
        trip.crew_needed += 1
        trip.save()
