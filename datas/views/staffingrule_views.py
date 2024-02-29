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
    filterset_fields = ['staffing_rule_count','staffing_rule_comment']
    # filterset_fields = ['staffing_rule_asset','staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']
