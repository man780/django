from rest_framework import generics
from rest_framework.response import Response
from .models import Entity
from .serializers import EntitySerializer, EntityFullSerializer, EntityFull2Serializer


class EntityList(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityCreate(generics.CreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityFullList(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntityFullSerializer


class EntityFull2List(generics.ListAPIView):
    queryset = Entity.objects.all()

    def list(self, data):
        queryset = self.get_queryset()
        new_response: list = []
        for item in queryset:
            item_properties: dict = {}
            for property in item.properties.all():
                item_properties[property.key] = property.value
            new_response.append(
                {
                    'value': item.value,
                    'properties': item_properties
                }
            )
        return Response(new_response)
