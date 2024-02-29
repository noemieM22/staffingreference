from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from datas.models import *
from datas.serializers import *

class Entity_Type_APIView(viewsets.ModelViewSet):

    queryset = Entity_type.objects.all()
    serializer_class = Entity_Type_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['entity_type_FR']

class Entity_APIView(viewsets.ModelViewSet):

    queryset = Entity.objects.all()
    serializer_class = Entity_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['entity_FR','entity_type']
