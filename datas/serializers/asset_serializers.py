from rest_framework import  serializers
from rest_framework.renderers import JSONRenderer

from datas.models.asset import *


class Asset_Category_Serializer(serializers.HyperlinkedModelSerializer):
    asset_category_parent = serializers.SerializerMethodField()

    class Meta:
        model = Asset_category
        fields = ['asset_category_FR','asset_category_parent']
    def get_asset_category_parent(self,obj):
        asset_category_parent= ''
        if(obj.asset_category_parent):
            asset_category_parent = obj.asset_category_parent.asset_category_FR
        return asset_category_parent

class Asset_Type_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Asset_type
        fields = ['asset_type_FR']

class Asset_Serializer(serializers.HyperlinkedModelSerializer):
    asset_type = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ['asset_FR','asset_type','asset_loan',]
        # fields = ['asset_FR','asset_category','asset_type','asset_loan']
    def get_update(self,obj):
        if(obj.type ==0):
            adr = 'updateAssetServer'
        else:
            adr = 'updateAssetBdd'
        # resultUpdate = '  <a href = "/appli/' + adr + '/'+str(obj.id)+'"><i class="bi bi-pencil"></i></a><a href = "/appli/deleteAsset/'+str(obj.id)+'"><i class="bi bi-trash"></i></a>'
        resultUpdate = '<i class="menudots bi bi-three-dots"></i>'
        return resultUpdate
    def get_asset_type(self,obj):
        asset_type= ''
        if(obj.asset_type):
            sgbd = obj.asset_type.asset_type_FR
        return asset_type
