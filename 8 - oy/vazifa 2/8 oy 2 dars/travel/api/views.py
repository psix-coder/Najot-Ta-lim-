from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.request import Request

from rest_framework import generics

from .permissions import TravelPermission

from .models import Hotel, Klass, Travel

from serializers import HotelSerializer, KlassSerializer, TravelSerializer



class HotelView(APIView):
    queryset = Hotel.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request:Request, pk=None):
        if not pk:
            hotels = Hotel.objects.all()
            return Response(HotelSerializer(hotels, many=True).data)
        else:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response(HotelSerializer(hotel).data)
            except Exception as e:
                return Response(str(e), status=404)

    def post(self, request:Request, pk=None):
        if pk:
            return Response("Method post is not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hotel = serializer.save()
        return Response(HotelSerializer(hotel).data)

    def put(self, request:Request, pk=None):
        if not pk:
            return Response("METHOD put is nod allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            hotel = get_object_or_404(Hotel, pk=pk)
            serializer = HotelSerializer(deta=request.data)
            serializer.is_valid(raise_excaption=True)
            hotel = serializer.save()
            return Response(HotelSerializer(hotel).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request:Request, pk=None):
        if not pk:
            return Response("Method delete is not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            hotel = get_object_or_404(Hotel, pk=pk)
            return Response("Successfuly deleted!")
        except Exception as e:
            return Response(str(e), status=404)


class KlassView(APIView):
    queryset = Klass.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request:Request, pk=None):
        if not pk:
            klass = Klass.objects.all()
            return Response(KlassSerializer(klass).data)
        try:
            klass = Klass.objects.get(pk=pk)
            return Response(KlassSerializer(klass).data)
        except Exception as e:
            return Response(str(e), status=404)

    def post(self, request:Request, pk=None):
        if pk:
            return Response("Method post is nod allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_excaption=True)
        klass = serializer.save()
        return Response(KlassSerializer(klass).data)

    def put(self, request:Request, pk=None):
        if not pk:
            return Response("Method delete is not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            klass = get_object_or_404(Klass, pk=pk)

            serializer = KlassSerializer(data=request.data, instance=klass)
            serializer.is_valid(raise_excaption=True)
            klass = serializer.save()
            return Response(KlassSerializer(klass).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request:Request, pk=None):
        if not pk:
            return Response("Method post is nod allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            klass = get_object_or_404(Klass, pk=pk)
            klass.delete()
            return ResourceWarning("Successfult deleted! ")
        except Exception as e:
            return Response(str(e), status=404)


class TravelView(APIView):
    permission_classes = [TravelPermission]

    def get(self, request:Request, pk=None):
        if not pk:
            travels = Travel.objects.all()
            return Response(TravelSerializer(travels, many=True).data)
        try:
            travel = get_object_or_404(Travel, pk=pk)
            self.chek_object.permissions(request, travel)
            return Response(TravelSerializer(travel).data)
        except Exception as e:
            return Response(str(e), status=404)

    def post(self, request:Request, pk=None):
        if pk:
            return Response("Method post is nod allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_excation=True)
        travel = serializer.save()
        return Response(TravelSerializer(travel).data)

    def put(self, request:Request, pk=None):
        if not pk:
            return Response("Method post is nod allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            travel = get_object_or_404(Travel, pk=pk)
            self.check_object_permissions(request, travel)
            serializer = TravelSerializer(data=request.data, instance=travel)
            serializer.is_valid(raise_exception=True)
            travel = serializer.save()
            return Response(TravelSerializer(travel).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk=None):
        if not pk:
            return Response("Method DELETE is not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            travel = get_object_or_404(Travel, pk=pk)
            self.check_object_permissions(request, travel)
            travel.delete()
            return Response("Successfully deleted!")
        except Exception as e:
            return Response(str(e), status=404)


class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
    lookup_url_kwarg = "klass_id"
    lookup_field = "pk"

    def get_queryset(self):
        return Klass.objects.all()

class KlassAPIVEW(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
    lookup_url_kwarg = "klass_id"
    lookup_field = "pk"

    def get_queryset(self):
        return Klass.objects.all()