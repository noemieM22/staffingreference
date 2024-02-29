
from django.urls import path, include
from datas.views import *
from rest_framework import routers
from . import views

app_name = 'datas'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'asset', Asset_APIView)
router.register(r'assetcategory', Asset_Category_APIView)
router.register(r'assettype', Asset_Type_APIView)

router.register(r'entitytype', Entity_Type_APIView)
router.register(r'entity', Entity_APIView)

router.register(r'staffingusetype', Staffing_Use_Type_APIView)
router.register(r'staffingrule', Staffing_Rule_APIView)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls
