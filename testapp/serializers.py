from .models import User, Todo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "date_of_birth"]

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name", "description", "user", "priority"]
