from django.urls import path, include
from rest_framework import routers
from recordings import views

router = routers.DefaultRouter()
router.register(r'recordings-data', views.RecordingsDataView, 'Recordings-Data')
router.register(r'categories', views.CategoriesView, 'Categories')
router.register(r'authors', views.AuthorsView, 'Authors')
router.register(r'tags', views.TagView, 'Tags')
router.register(r'recordings', views.RecordingsView, 'Recordings')

urlpatterns = [
    path('v1/', include(router.urls)),  
]