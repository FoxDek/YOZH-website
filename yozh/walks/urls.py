from django.urls import path
from .views import WalkListCreate, WalkRetrieveUpdateDestroy, walk_form

urlpatterns = [
    path('walks/', WalkListCreate.as_view(), name='walks-list-create'),
    path('walks/<int:pk>/', WalkRetrieveUpdateDestroy.as_view(), name='walks-detail'),
    path('walks/new/', walk_form, name='walk-form'),
]
