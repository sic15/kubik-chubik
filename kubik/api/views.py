
from django.shortcuts import render
from rest_framework import generics, status, viewsets

from user.models import User
from course.models import Course
from .serializers import UserSerializer, TeacherSerializer, CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(type='teacher')
    serializer_class = TeacherSerializer
  #  serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(type='student')
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
