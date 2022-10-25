from rest_framework import generics
from .models import Entity, Property
from .serializers import EntitySerializer


class EntityList(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
