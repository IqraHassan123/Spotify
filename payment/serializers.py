# import datetime
# from rest_framework import serializers
#
#
# def check_expiry_month(value):
#     if not 1 <= int(value) <= 12:
#         raise serializers.ValidationError("Expire Month")
#
# def check_expiry_year(value):
#     today=datetime.datetime.now()
#     if not value >= today.year:
#         raise serializers.ValidationError("Expire Year")
#
# def check_expiry_cvc(value):
#     if not 3 <= len(str(value)) <= 4:
#         raise serializers.ValidationError("Invalid CVC")
#
# def check_payment_method(value):
#     payment_method=value.lower()
#     if payment_method not in ["card"]:
#         raise serializers.ValidationError("Invalid Payment Method")
#
# class CardInformationSerializer(serializers.Serializer):
#     card_number=serializers.CharField(
#         label="Card Number"
#     )
#     expiry_month=serializers.IntegerField(
#         label="Expiry Month",
#     validators = [check_expiry_month],
#     )
#     expiry_year=serializers.IntegerField(
#         label="Expiry Year",
#     validators = [check_expiry_year],
#     )
#     cvc=serializers.IntegerField(
#         label="CVC",
#     validators = [check_expiry_cvc],
#     )
from rest_framework import serializers

from .models import Payment, PaymentConfigurations


class PaymentSerializer(serializers.ModelSerializer):
    transaction_type = serializers.ReadOnlyField()
    transaction_amount = serializers.ReadOnlyField()

    """
    A custom serializer to handle Order Payments
    """
    class Meta:
        model = Payment
        fields = ('id', 'details', 'transaction_type', 'transaction_amount', 'created_at', 'source', 'receiver', 'amount')
        depth = 2


class PaymentConfigurationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConfigurations
        fields = '__all__'

