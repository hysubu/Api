from rest_framework import serializers
from app1 .models import Student

def fst_letter(value):
    if value[0] != 'r' :
        raise serializers.ValidationError('name start with r')
    return value


class Studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100,validators = [fst_letter])
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name',instance.name)
        instance.age= validated_data.get('age',instance.age)
        instance.city= validated_data.get('city',instance.city)
        instance.save()
        return instance

    def validate_age(self, value):
        if value >= 30 :
            raise serializers.ValidationError('Age is not Avilabel')
        return value

    def validate(self, data):
        nm = data.get('name')
        city = data.get('city')
        if nm.upper() == 'SUBU' and city != 'bhubaneswar':
            raise serializers.ValidationError('city must be reach')
        return data 


    # def fst_letter(value):
    #     if value[0] != 'r' :
    #         raise serializers.ValidationError('name start with r ')
    #     return value