from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    This class is a `Serializer` that converts the data from the database 
    into JSON format."""
    class Meta:
        model = Student
        fields = '__all__'
