
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'app'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    #path('', include(router.urls)),
    path('asset',views.Asset_View.as_view(), name ='Asset'),
    path('asset-type/',views.Asset_Type_View.as_view(), name ='Asset-type'),
    path('asset-category/',views.Asset_Category_View.as_view(), name ='Asset-category'),

    path('entity',views.Entity_View.as_view(), name ='Entity'),
    path('entity-type/',views.Entity_Type_View.as_view(), name ='Entity-type'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
