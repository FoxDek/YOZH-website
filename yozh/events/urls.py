from django.urls import path
from .views import EventListCreate, EventRetrieveUpdateDestroy, event_form

urlpatterns = [
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name='event-detail'),
    path('events/new/', event_form, name='event-form'),
]
