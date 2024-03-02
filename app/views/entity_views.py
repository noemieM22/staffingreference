from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

import json

from datas.models import Entity
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Entity_View(CreateView):
    model = Entity
    form_class = Entity_Form
    template_name = 'datas_references.html'
    success_url = reverse_lazy('app:Entity')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['Entity'] = 'active'
        data['tableToDisplay'] = 'Entity'
        return data

class Entity_Type_View(CreateView):
    model = Entity_type
    form_class = Entity_Type_Form
    template_name = 'datas_references.html'
    success_url = reverse_lazy('app:Entity-type')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['Entitytype'] = 'active'
        data['tableToDisplay'] = 'Entity_type'
        # data['fields']= get_fields_name(Entity_type)
        return data
