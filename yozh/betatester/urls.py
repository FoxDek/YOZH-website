from django.urls import path
from .views import BetaTesterTicketLC, BetaTesterTicketRUD

urlpatterns = [
    path('betatester/', BetaTesterTicketLC.as_view(), name='betatester-list-create'),
    path('betatester/<int:pk>/', BetaTesterTicketRUD.as_view(), name='betatester-detail'),
]
