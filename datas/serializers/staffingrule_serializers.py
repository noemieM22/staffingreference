from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer

from datas.models.staffingrule import *

# use : individuel, partagé...
class Staffing_Use_Type_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Staffing_use_type
        fields = ['staffing_use_type_FR']

class Staffing_Rule_Serializer(serializers.HyperlinkedModelSerializer):
    staffing_rule_asset = serializers.SerializerMethodField()
    staffing_rule_entity = serializers.SerializerMethodField()
    staffing_rule_type = serializers.SerializerMethodField()

    class Meta:
        model = Staffing_rule
        fields = ['staffing_rule_asset','staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']
        # fields = ['staffing_rule_asset','staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']
    def get_staffing_rule_asset(self,obj):
        return obj.staffing_rule_asset.asset_FR
    def get_staffing_rule_entity(self,obj):
        return obj.staffing_rule_entity.entity_FR
    def get_staffing_rule_type(self,obj):
        return obj.staffing_rule_type.staffing_use_type_FR
