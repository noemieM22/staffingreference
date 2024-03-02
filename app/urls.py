
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
    path('',views.Staffing_rule_View.as_view(), name ='Rule'),
    path('rule-type',views.Staffing_use_type_View.as_view(), name ='Rule-type'),

    path('staffing-rule/update/<int:pk>',views.Staffing_rule_update_View.as_view(), name ='Rule-update'),
    path('staffing-use-type/update/<int:pk>',views.Staffing_use_type_update_View.as_view(), name ='Entity-type-update'),

    path('staffing-rule/delete/<int:pk>',views.Staffing_rule_delete_View.as_view(), name ='Rule-delete'),
    path('staffing-use-type/delete/<int:pk>',views.Staffing_use_type_delete_View.as_view(), name ='Entity-type-delete'),
        path('asset',views.Asset_View.as_view(), name ='Asset'),
    path('asset-type/',views.Asset_Type_View.as_view(), name ='Asset-type'),
    path('asset-category/',views.Asset_Category_View.as_view(), name ='Asset-category'),

    path('asset/update/<int:pk>',views.Asset_update_View.as_view(), name ='Asset-update'),
    path('asset-type/update/<int:pk>',views.Asset_type_update_View.as_view(), name ='Asset-type-update'),
    path('asset-category/update/<int:pk>',views.Asset_category_update_View.as_view(), name ='Asset-category-update'),

    path('asset/delete/<int:pk>',views.Asset_delete_View.as_view(), name ='Asset'),
    path('asset-type/delete/<int:pk>',views.Asset_type_delete_View.as_view(), name ='Asset-type-delete'),
    path('asset-category/delete/<int:pk>',views.Asset_category_delete_View.as_view(), name ='Asset-category-delete'),


    path('entity',views.Entity_View.as_view(), name ='Entity'),
    path('entity-type/',views.Entity_Type_View.as_view(), name ='Entity-type'),

    path('entity/update/<int:pk>',views.Entity_update_View.as_view(), name ='Entity-update'),
    path('entity-type/update/<int:pk>',views.Entity_type_update_View.as_view(), name ='Entity-type-update'),

    path('entity/delete/<int:pk>',views.Entity_delete_View.as_view(), name ='Entity-delete'),
    path('entity-type/delete/<int:pk>',views.Entity_type_delete_View.as_view(), name ='Entity-type-delete'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
