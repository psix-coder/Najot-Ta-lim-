from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Book
from .serializers import BookSerializer, GenreSerializer


class HomeView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            books = Book.objects.all()
            return Response(BookSerializer(books, many=True).data)
        else:
            try:
                book = Book.objects.get(pk=pk)
                return Response(BookSerializer(book).data)
            except Exception as e:
                return Response(str(e), status=404)

    def post(self, request: Request, pk=None):
        if pk:
            return Response("Method Post is not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = Book.objects.create(**serializer.validated_data)
        return Response(BookSerializer(book).data)


class GenreView(APIView):
    def get(self, request, pk=None):
        if not pk:
            genres = Genre.objects.all()
            return Response(GenreSerializer(genres, many=True).data)
        else:
            try:
                genre = Genre.objects.get(pk=pk)
                return Response(GenreSerializer(genre).data)
            except Exception as e:
                return Response(str(e), status=404)

    def post(self, request, pk=None):
        if pk:
            return Response("Method Post is not Allowed!!!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = Genre.objects.create(**serializer.validated_data)
        return Response(GenreSerializer(genre).data)
