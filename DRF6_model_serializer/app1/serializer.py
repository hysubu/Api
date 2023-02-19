from rest_framework import serializers
from app1 .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)