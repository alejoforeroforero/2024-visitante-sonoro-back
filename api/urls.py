from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/recordings/', include('recordings.urls')),
    path('api/auth/', include('credentials.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
