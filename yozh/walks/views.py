from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Walk
from .serializers import WalkSerializer, WalkCreateSerializer
from django.shortcuts import render

def walk_form(request):
    return render(request, 'walks/walk_form.html')

class WalkListCreate(generics.ListCreateAPIView):
    queryset = Walk.objects.all()
    serializer_class = WalkCreateSerializer
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WalkCreateSerializer
        return WalkSerializer

class WalkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
