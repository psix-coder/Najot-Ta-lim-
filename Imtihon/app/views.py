from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import *
from .serializers import (
    TypeCourseSerializer, CourseSerializer, CommentSerializer,
    LessonSerializer, LessonVideoSerializer, TeachersSerializer, UserSerializer, RatingSerializer, CommentDetailSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsTeacher, IsAuthenticatedUser, IsStudent

from django.core.mail import send_mail
from django.contrib.auth import get_user_model




class TypeCourseViewSet(viewsets.ModelViewSet):
    queryset = TypeCourse.objects.all()
    serializer_class = TypeCourseSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonViewSet(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacher]


class LessonVideoViewSet(generics.ListCreateAPIView):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer
    permission_classes = [IsTeacher]


class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | permissions.IsAdminUser]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsTeacher | IsStudent]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated | IsStudent]



class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsTeacher()]
        return [AllowAny()]
    
    def perform_create(self, serializer):
        course = CourseSerializer(serializer.save()).data
        
        subject = "Yangi dars qo'shildi, marhamat tanishib chiqing"
        message = f"Dars mavzusi: {course.get('title')}"
        
        recipient_list = list(get_user_model().objects.values_list('email', flat=True))
        
        if recipient_list:
            send_mail(
                subject=subject,
                message=message,
                from_email='xolmatovjamoliddin588@gmail.com',
                recipient_list=recipient_list,
                fail_silently=False
            )





class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsStudent | IsTeacher]


class RatingViewSet(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)
    

