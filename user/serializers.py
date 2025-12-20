from rest_framework import serializers 
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data["email"],
            username=validated_data["username"],
            is_active=validated_data.get("is_active", True),
            is_admin=validated_data.get("is_admin", False),
            is_staff=validated_data.get("is_staff", False),
            is_superuser=validated_data.get("is_superuser", False),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 150)
    password = serializers.CharField(max_length = 150)
    class Meta:
        Model = CustomUser
        fields = ["email", "password"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username"]
