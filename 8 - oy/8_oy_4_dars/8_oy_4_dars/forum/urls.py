from django.urls import path
from .views import TopicApiView, TopicDetailApiView, CommentApiView, CommentDetailApiView

urlpatterns = [
    path('topics/', TopicApiView.as_view()),
    path('topics/<int:pk>', TopicDetailApiView.as_view()),

    path('comments/', CommentApiView.as_view()),
    path('comments/<int:pk>', CommentDetailApiView.as_view()),
]

