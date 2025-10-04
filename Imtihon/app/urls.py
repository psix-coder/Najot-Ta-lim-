from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TypeCourseViewSet, CourseViewSet, LessonViewSet,
    LessonVideoViewSet, TeachersViewSet, CommentViewSet,
    UserViewSet, RatingViewSet, CourseListCreateView, CommentDetailView
)

router = DefaultRouter()
router.register(r'type-courses', TypeCourseViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'teachers', TeachersViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    
    path('lessons/', LessonViewSet.as_view(), name='lesson-list'),
    path('lesson-videos/', LessonVideoViewSet.as_view(), name='lesson-video-list'),
    path('course-list/', CourseListCreateView.as_view(), name='course-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('ratings/', RatingViewSet.as_view(), name='rating-list-create'),
]