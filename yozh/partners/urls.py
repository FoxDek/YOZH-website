from django.urls import path
from .views import PartnerTicketLC, PartnerTicketRUD

urlpatterns = [
    path('partner-tickets/', PartnerTicketLC.as_view(), name='partner-ticket-list-create'),
    path('partner-tickets/<int:pk>/', PartnerTicketRUD.as_view(), name='partner-ticket-detail'),
]
