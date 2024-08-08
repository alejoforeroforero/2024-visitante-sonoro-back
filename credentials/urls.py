from django.contrib import admin
from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    RegisterView,
    UserView,
    LogoutView,
    UpdateProfilePictureView,
    UpdateFavoriteRecordsView,
    GoogleSignInView
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-profile-picture/', UpdateProfilePictureView.as_view(), name='update_profile_picture'),
    path('google-signin/', GoogleSignInView.as_view(), name='google_signin'),
    path('favorites/', UpdateFavoriteRecordsView.as_view(), name='logout'),
]
