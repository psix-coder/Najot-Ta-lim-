from rest_framework import permissions, viewsets
from .models import Foods, FoodType, Comment
from .serializers import FoodsSerializer, FoodDetailSerializer, FoodTypeSerializer, CommentSerializer


class FoodsViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FoodDetailSerializer
        return FoodsSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]