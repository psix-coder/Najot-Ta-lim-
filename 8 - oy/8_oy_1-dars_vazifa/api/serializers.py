from rest_framework import serializers


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    about = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    page = serializers.IntegerField(default=50)
    published = serializers.DateTimeField()
    genre_id = serializers.IntegerField()
