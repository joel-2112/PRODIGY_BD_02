from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email address")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long")
        if value.isdigit():
            raise serializers.ValidationError("Username cannot be entirely numeric")
        return value
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("There is not negative age")
        return value
