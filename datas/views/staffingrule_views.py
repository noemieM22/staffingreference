from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from datas.models import *
from datas.serializers import *

class Staffing_Use_Type_APIView(viewsets.ModelViewSet):

    queryset = Staffing_use_type.objects.all()
    serializer_class = Staffing_Use_Type_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['staffing_use_type_FR']

class Staffing_Rule_APIView(viewsets.ModelViewSet):

    queryset = Staffing_rule.objects.all()
    serializer_class = Staffing_Rule_Serializer

    filter_backends = [DjangoFilterBackend]
    fields = ['update','staffing_rule_asset','staffing_rule_entity_type','staffing_rule_entity_type_FR','staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Staffing_rule.objects.all()
        staffing_rule_entity_type = self.request.query_params.get('staffing_rule_entity_type')
        if(staffing_rule_entity_type):
            queryset = queryset.filter(staffing_rule_entity__entity_type_id=staffing_rule_entity_type)

        return queryset
