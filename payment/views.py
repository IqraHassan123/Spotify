from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer,PaymentConfigurationsSerializer
from .models import PaymentConfigurations



class PaymentListView(APIView):


    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this view

    def get(self, request):

        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(APIView):
    """
    Retrieve, update, or delete a payment.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve a specific payment.
        """
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific payment.
        """
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(payment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific payment.
        """
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentConfigurationsListView(APIView):
    """
    List all payment configurations or create a new one.
    """

    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get(self, request):
        """
        List all payment configurations
        """
        payment_configs = PaymentConfigurations.objects.all()
        serializer = PaymentConfigurationsSerializer(payment_configs, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new payment configuration.
        """
        serializer = PaymentConfigurationsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentConfigurationsDetailView(APIView):
    """
    Retrieve, update, or delete a specific payment configuration.
    """

    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request, pk):
        """
        Retrieve a specific payment configuration.
        """
        try:
            payment_config = PaymentConfigurations.objects.get(pk=pk)
        except PaymentConfigurations.DoesNotExist:
            return Response({"error": "Payment configuration not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentConfigurationsSerializer(payment_config)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific payment configuration.
        """
        try:
            payment_config = PaymentConfigurations.objects.get(pk=pk)
        except PaymentConfigurations.DoesNotExist:
            return Response({"error": "Payment configuration not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentConfigurationsSerializer(payment_config, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific payment configuration.
        """
        try:
            payment_config = PaymentConfigurations.objects.get(pk=pk)
        except PaymentConfigurations.DoesNotExist:
            return Response({"error": "Payment configuration not found."}, status=status.HTTP_404_NOT_FOUND)

        payment_config.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
