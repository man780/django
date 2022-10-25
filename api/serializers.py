from rest_framework import serializers
from .models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('key', 'value')
        model = Property


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'value', 'modified_by')
        model = Entity


class EntityCreateSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(required=True)

    class Meta:
        fields = ('value', )
        model = Entity
