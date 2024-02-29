from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from datas.models import *
from datas.serializers import *

class Asset_Category_APIView(viewsets.ModelViewSet):

    queryset = Asset_category.objects.all()
    serializer_class = Asset_Category_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['asset_category_FR','asset_category_level']

class Asset_Type_APIView(viewsets.ModelViewSet):

    queryset = Asset_type.objects.all()
    serializer_class = Asset_Type_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['asset_type_FR']


class Asset_APIView(viewsets.ModelViewSet):

    queryset = Asset.objects.all()
    serializer_class = Asset_Serializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['asset_FR']
    # filterset_fields = ['asset_FR','asset_category','asset_type','asset_loan']
