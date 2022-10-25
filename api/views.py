from rest_framework import generics
from .models import Entity, Property
from .serializers import EntitySerializer


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
