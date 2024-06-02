from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('partners.urls')),    # партнёры (маршрут)
    path('api/', include('events.urls')),
    path('api/', include('walks.urls')),
    path('api/', include('betatester.urls')),  # маршруты для тикетов бетатестеров
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)