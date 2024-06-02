from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Event
from .serializers import EventSerializer, EventCreateSerializer
from django.shortcuts import render

def event_form(request):
    return render(request, 'events/event_form.html')
class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EventCreateSerializer
        return EventSerializer

class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
