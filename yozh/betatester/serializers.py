from rest_framework import serializers
from .models import BetaTesterTicket

class BetaTesterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetaTesterTicket
        fields = '__all__'
