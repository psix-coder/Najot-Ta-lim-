from rest_framework import serializers

from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TypeCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCourse
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['lesson', 'content', 'user']


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'lesson', 'created_at']



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user']