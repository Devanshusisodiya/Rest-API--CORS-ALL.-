from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer
# Create your views here.

@api_view(['GET'])
def basePoint(request):
    return Response('API Base Point - webdev')

# create views to browse through the api

@api_view(['GET'])
def getTesting(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postTeacherSingular(request, email, password):
    teacher = Teacher.objects.get(email=email, password=password)
    serializer = TeacherSerializer(teacher, many=False)
    return Response(serializer.data['name'])