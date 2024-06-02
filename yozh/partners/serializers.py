from rest_framework import serializers
from .models import PartnerTicket

class PartnerTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerTicket
        fields = '__all__'
