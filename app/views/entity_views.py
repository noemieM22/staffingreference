from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

import json

from datas.models import Asset
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Asset_View(CreateView):
    model = Asset
    form_class = Asset_Form
    template_name = 'menu_asset.html'
    success_url = reverse_lazy('app:Asset')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['asset'] = 'active'
        data['tableToDisplay'] = 'Asset'
        return data

class Asset_Type_View(CreateView):
    model = Asset_type
    form_class = Asset_Type_Form
    template_name = 'menu_asset.html'
    success_url = reverse_lazy('app:Asset-type')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['assettype'] = 'active'
        data['urlasset'] = '/datas/assettype/'
        data['tableToDisplay'] = 'Asset_type'
        # data['fields']= get_fields_name(Asset_type)
        return data

class Asset_Category_View(CreateView):
    model = Asset_category
    form_class = Asset_Category_Form
    template_name = 'menu_asset.html'
    success_url = reverse_lazy('app:Asset-category')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['assetcategory'] = 'active'
        data['urlasset'] = '/datas/assetcategory/'
        data['tableToDisplay'] = 'Asset_category'
        # data['fields']= get_fields_name(Asset_type)
        return data
