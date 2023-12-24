from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerevalAddedSerializer,UserSerializer,CoordsSerializer,SprActivitiesTypesSerializer,PerevalImagesSerializer,PerevalAreasSerializer
from django.shortcuts import get_object_or_404
from .models import User, Coords, PerevalAdded, PerevalImages, PerevalAreas, SprActivitiesTypes

class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            pereval = get_object_or_404(PerevalAdded, pk=id)
            serializer = PerevalAddedSerializer(pereval)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, *args, **kwargs):
        pereval = get_object_or_404(PerevalAdded, pk=id)
        if pereval.status != 'new':
            return Response({"state": 0, "message": "Cannot edit, not in 'new' status"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = PerevalAddedSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": 1, "message": "Updated successfully"})
        return Response({"state": 0, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            user = get_object_or_404(User, pk=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CoordsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CoordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            coords = get_object_or_404(Coords, pk=id)
            serializer = CoordsSerializer(coords)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class PerevalImagesView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PerevalImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            image = get_object_or_404(PerevalImages, pk=id)
            serializer = PerevalImagesSerializer(image)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class PerevalAreasView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PerevalAreasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            area = get_object_or_404(PerevalAreas, pk=id)
            serializer = PerevalAreasSerializer(area)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class SprActivitiesTypesView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SprActivitiesTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            activity_type = get_object_or_404(SprActivitiesTypes, pk=id)
            serializer = SprActivitiesTypesSerializer(activity_type)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)



