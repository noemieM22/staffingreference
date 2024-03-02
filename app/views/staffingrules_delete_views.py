from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

import json

from datas.models import Staffing_rule
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Staffing_rule_delete_View(DeleteView):

    model = Staffing_rule
    fields = "__all__"


    def get(self,request,pk):
        rules = 'active'
        instance = Staffing_rule.objects.get(id=pk)
        form = Staffing_rule_Form(instance=instance)
        return render(request, 'datas_delete.html',{'rules':rules,'form':form})

    def get_success_url(self):
        return reverse('app:Rule')

class Staffing_use_type_delete_View(DeleteView):

    model = Staffing_use_type
    fields = "__all__"

    def get(self,request,pk):
        rules = 'active'
        instance = Staffing_use_type.objects.get(id=pk)
        form = Staffing_use_type_Form(instance=instance)
        return render(request, 'datas_delete.html',{'rules':rules,'form':form})

    def get_success_url(self):
        return reverse('app:Rule-type')
