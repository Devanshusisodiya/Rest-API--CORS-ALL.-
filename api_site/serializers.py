from rest_framework import serializers
from .models import Teacher
from .models import Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'password')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'email', 'password')
