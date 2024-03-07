from rest_framework import serializers
from .models import CustomUser
from.otp_generator import generate_otp


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "email", "name", "password", "otp"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
            otp=generate_otp()
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
