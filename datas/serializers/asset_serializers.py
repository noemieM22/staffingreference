from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer

from datas.models.asset import *


class Asset_Category_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Asset_category
        fields = ['asset_category_FR','asset_category_level']

class Asset_Type_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Asset_type
        fields = ['asset_type_FR']

class Asset_Serializer(serializers.HyperlinkedModelSerializer):
    entity_type = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ['asset_FR']
        # fields = ['asset_FR','asset_category','asset_type','asset_loan']
