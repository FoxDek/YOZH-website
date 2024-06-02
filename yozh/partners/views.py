from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import PartnerTicket
from .serializers import PartnerTicketSerializer

class PartnerTicketLC(generics.ListCreateAPIView):
    queryset = PartnerTicket.objects.all()
    serializer_class = PartnerTicketSerializer
    pagination_class = PageNumberPagination

class PartnerTicketRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartnerTicket.objects.all()
    serializer_class = PartnerTicketSerializer
