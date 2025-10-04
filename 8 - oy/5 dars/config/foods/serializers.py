from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Foods, Comment, FoodType


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = "__all__"
        read_only_fields = ["pk"] 


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_name = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True
    )
    food = serializers.StringRelatedField(read_only=True)
    food_name = serializers.PrimaryKeyRelatedField(
        queryset=Foods.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["pk"]


class FoodsSerializer(serializers.ModelSerializer):
    food_type = serializers.StringRelatedField(read_only=True)
    food_type_name = serializers.PrimaryKeyRelatedField(
        queryset=FoodType.objects.all(), source='food_type', write_only=True
    )

    class Meta:
        model = Foods
        fields = "__all__"
        read_only_fields = ["pk"]


class FoodDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    food_type = FoodTypeSerializer(read_only=True)

    class Meta:
        model = Foods
        fields = "__all__"
        read_only_fields = ["pk"]