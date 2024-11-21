from django.db import models

from accounts.models import UUIDModel,User

class Payment(UUIDModel):

    source = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='source')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='receiver')
    amount = models.FloatField(null=True)
    details = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.source.email + ' - ' + self.receiver.email + self.details


class PaymentConfigurations(UUIDModel):
    MONTHLY = 'monthly'
    WEEKLY = 'weekly'

    PLAN_CHOICES = [
        (MONTHLY, 'Monthly'),
        (WEEKLY, 'Weekly'),
    ]

    plan = models.CharField(
        max_length=10,
        choices=PLAN_CHOICES,
        default=MONTHLY,
    )

    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.get_plan_display()} - ${self.price}"

