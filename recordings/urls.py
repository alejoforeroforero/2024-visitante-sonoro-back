from django.urls import path, include
from rest_framework import routers
from recordings import views



router = routers.DefaultRouter()
router.register(r'recordings-data', views.RecordingsDataView, 'Recordings-Data')
router.register(r'categories', views.CategoriesView, 'Categories')
router.register(r'authors-data', views.AuthorsView, 'Authors-Data')
router.register(r'authors', views.AuthorsViewFront, 'Authors')
router.register(r'tags', views.TagView, 'Tags')
router.register(r'recordings', views.RecordingsView, 'Recordings')
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  
]