from rest_framework import generics
from rest_framework import permissions


from .models import Topic, Comment
from .serializers import TopicSerializer, CommentSerializer


class TopicApiView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class CommentApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
