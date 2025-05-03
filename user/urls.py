from django.urls import path
from .views import UserRegistration, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
    
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', UserRegistration.as_view(), name='new-user-register'),
    path('login/',    LoginView.as_view(),        name='token_obtain_pair'),
]

