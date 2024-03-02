from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

import json

from datas.models.staffingrule import *
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Staffing_rule_View(CreateView):
    model = Staffing_rule
    form_class = Staffing_rule_Form
    template_name = 'staffing_rule.html'
    success_url = reverse_lazy('app:Rule')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['tableToDisplay'] = 'Staffing_rule'
        return data


class Staffing_use_type_View(CreateView):
    model = Staffing_use_type
    form_class = Staffing_use_type_Form
    template_name = 'datas_references.html'
    success_url = reverse_lazy('app:Rule-type')

    def get_context_data(self, *args,**kwargs):
        data = super().get_context_data(**kwargs)
        # choix de l'onglet actif
        data['rules'] = 'active'
        data['tableToDisplay'] = 'Staffing_use_type'
        return data
