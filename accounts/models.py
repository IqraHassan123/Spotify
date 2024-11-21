import uuid
from djstripe.models import Customer, Account
from django.db import models
from django.contrib.auth.models import AbstractUser
from .enum import UserRole
from django.conf import settings

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField("Email of User", max_length=255, unique=True)
    stripe_customer = models.ForeignKey(
        'djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists"
    )
    stripe_account = models.ForeignKey(
        'djstripe.Account', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Account object, if it exists"
    )

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=UserRole.choices())
    is_premium = models.BooleanField(default=False)

    # Add related_name to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Change related name here
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Change related name here
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"



