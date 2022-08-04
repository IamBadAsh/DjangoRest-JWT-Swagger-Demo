from rest_framework import routers, serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages = {"Password_Error":"Something went wrong check password"}
    )

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
