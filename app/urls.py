
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
    # path('asset_category',views.Asset_category_View.as_view(), name ='Asset_category'),
    path('',views.Asset_category_View.as_view(), name ='Asset_category'),

    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
