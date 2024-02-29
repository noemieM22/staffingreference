from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

import json

from datas.models import Asset
from app.forms import *

class Asset_category_View(CreateView):
    model = Asset_category
    form_class = Asset_category_Form
    template_name = 'menu_asset.html'
    success_url = reverse_lazy('app:Asset_category')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['server'] = 'active'
        data['bdd'] = ''
        return data


        # asset = Asset.objects.get(id=body[0])
        #
        # if (asset.sgbd.id ==2):
        #     listTablePostgres(asset)
