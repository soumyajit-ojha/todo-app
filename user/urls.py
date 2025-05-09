from django.urls import path
from .views import (
    RegistrationAPIView,
    UserLoginAPIView,
    ProfileAPIView,
    AllUserProfileAPIView
)
    


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='new-user-register'),
    path('login/', UserLoginAPIView.as_view(), name='token_obtain_pair'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('profile/all/', AllUserProfileAPIView.as_view(), name='all-profile'),
]

