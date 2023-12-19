from rest_framework import serializers
from .models import User, Coords, PerevalAdded, PerevalImages, PerevalAreas, SprActivitiesTypes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'

class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'

class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'

class PerevalAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = '__all__'

class SprActivitiesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprActivitiesTypes
        fields = '__all__'
