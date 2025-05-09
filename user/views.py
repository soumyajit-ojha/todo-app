from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate



from .models import CustomUser
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
)


def get_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class RegistrationAPIView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = get_token(user)


            return Response({"token":token, "messag":"Registeration successful."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class UserLoginAPIView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                email = serializer.data.get("email")
                password = serializer.data.get("password")

                user = authenticate(email=email, password=password)
                token = get_token(user)

                if not user:
                    return Response({"message" : "email and password are not valid."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"token":token, "message" : "Logged in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            print(request.data)
            serializer = ProfileSerializer(instance=request.user)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class AllUserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            all_users = CustomUser.objects.all()
            serializer = ProfileSerializer(all_users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
