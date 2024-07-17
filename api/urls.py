from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recordings.urls')),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
