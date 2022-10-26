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

    def to_internal_value(self, data):
        result: dict = {}
        request_data = data.get('data')
        if request_data:
            result['value'] = request_data.get('value')
        return result
