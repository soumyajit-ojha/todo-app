from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import UserSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.email

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # (optional) add extra claims
        token['username'] = user.username
        return token
    

class UserRegistration(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class LoginView(TokenObtainPairView):
    """
    request: { "email": "...", "password": "..." }
    response: { "access": "...", "refresh": "..." }
    """
    serializer_class = CustomTokenObtainPairSerializer