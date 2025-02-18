from rest_framework import serializers
from .models import User
class UserSerializer(serializers.Serializer):
    class meta:
        model = User
        fields = ['name','email','age']
# Compare this snippet from task02/users/views.py:

