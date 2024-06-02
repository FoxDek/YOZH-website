from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import BetaTesterTicket
from .serializers import BetaTesterTicketSerializer

class BetaTesterTicketLC(generics.ListCreateAPIView):
    queryset = BetaTesterTicket.objects.all()
    serializer_class = BetaTesterTicketSerializer
    pagination_class = PageNumberPagination

class BetaTesterTicketRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetaTesterTicket.objects.all()
    serializer_class = BetaTesterTicketSerializer
