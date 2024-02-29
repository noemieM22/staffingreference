from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer

from datas.models.entity import *


class Entity_Type_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entity_type
        fields = ['entity_type_FR']

class Entity_Serializer(serializers.HyperlinkedModelSerializer):
    entity_type = serializers.SerializerMethodField()
    class Meta:
        model = Entity
        fields = ['entity_FR','entity_type']
    def get_entity_type(self,obj):
        entity_type= Entity_type.objects.get(id=obj.entity_type.id)
        return entity_type.libelle
