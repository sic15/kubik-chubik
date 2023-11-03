from rest_framework import serializers

from user.models import User
from course.models import Course, TimeTable


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', "username", "email", "first_name", "last_name", "type")

class TeacherCoursesSerializer(serializers.ModelSerializer):
    class Model:
        model = Course
        fields = '__all__'

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields ='__all__'

class CourseSerializer(serializers.ModelSerializer):
    timetable = TimeTableSerializer(many=True)
    class Meta:
        model = Course
        fields ='__all__'


class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField(source='user.teacher' )
    class Meta:
        model = User
        fields = ('id', "username", "email", "first_name", "last_name", 'courses')

    
