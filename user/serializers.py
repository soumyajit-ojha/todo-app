from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
            "is_active",
            "is_admin",
            "is_staff",
            "is_superuser",
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
