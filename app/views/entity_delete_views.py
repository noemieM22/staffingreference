from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

import json

from datas.models import Entity
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Entity_delete_View(DeleteView):

    model = Entity
    fields = "__all__"


    def get(self,request,pk):
        entity = 'active'
        instance = Entity.objects.get(id=pk)
        form = Entity_Form(instance=instance)
        return render(request, 'datas_delete.html',{'Entity':entity,'form':form})

    def get_success_url(self):
        return reverse('app:Entity')

class Entity_type_delete_View(DeleteView):

    model = Entity_type
    fields = "__all__"

    def get(self,request,pk):
        entity = 'active'
        instance = Entity_type.objects.get(id=pk)
        form = Entity_Type_Form(instance=instance)
        return render(request, 'datas_delete.html',{'Entity':entity,'form':form})

    def get_success_url(self):
        return reverse('app:Entity-type')
