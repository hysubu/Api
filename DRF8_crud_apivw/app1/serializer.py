from rest_framework import serializers
from app1.models import Student

class Studentserializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = ['id','name','age','city']