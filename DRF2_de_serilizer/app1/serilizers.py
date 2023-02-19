from rest_framework import serializers 
from app1 .models import Student
class StudentSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


    def create(self,validate_data):
        return Student.objects.create(**validate_data)