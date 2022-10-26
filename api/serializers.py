from rest_framework import serializers
from .models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('key', 'value')
        model = Property


class EntitySerializer(serializers.ModelSerializer):
    data_value = serializers.SerializerMethodField('get_data_value')

    class Meta:
        fields = ('id', 'value', 'data_value', 'modified_by')
        model = Entity
        read_only_fields = ('id', 'modified_by')

    def get_data_value(self, obj):
        return obj.value


class EntityFullSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(read_only=True, many=True)

    class Meta:
        fields = ('value', 'properties')
        model = Entity


class EntityFull2Serializer(serializers.ModelSerializer):
    property_list = serializers.SerializerMethodField()

    def get_property_list(self, instance):
        names = []
        a = instance.properties.get_queryset()
        for i in a:
            names.append({i.key, i.value})
        return names

    class Meta:
        fields = ('value', 'property_list')
        model = Entity
