from django.urls import path
from .views import PaymentListView, PaymentDetailView, PaymentConfigurationsListView, PaymentConfigurationsDetailView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),  # List and create payments
    path('payments/<uuid:pk>/', PaymentDetailView.as_view(), name='payment-detail'),  # Retrieve, update, or delete a payment
    path('payment-configurations/', PaymentConfigurationsListView.as_view(), name='payment-config-list'),  # List and create payment configurations
    path('payment-configurations/<uuid:pk>/', PaymentConfigurationsDetailView.as_view(), name='payment-config-detail'),  # Retrieve, update, or delete a payment configuration
]
