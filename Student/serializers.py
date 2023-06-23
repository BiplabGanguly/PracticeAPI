from rest_framework import serializers
from .models import StudentClass

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'

    
    def validate(self, attrs):
        if attrs['roll'] == "00" or attrs['roll'] == "0":
            raise serializers.ValidationError({'error':'roll is not 0'})
        
        return attrs