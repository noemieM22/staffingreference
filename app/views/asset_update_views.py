from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

import json

from datas.models import Asset
from app.forms import *

# from datas.statics.datas_structure import get_fields_name

class Asset_update_View(UpdateView):

    model = Asset
    fields = "__all__"


    def get(self,request,pk):
        asset = 'active'
        instance = Asset.objects.get(id=pk)
        form = Asset_Form(instance=instance)
        return render(request, 'datas_update.html',{'asset':asset,'form':form})

    def get_success_url(self):
        return reverse('app:Asset')

class Asset_type_update_View(UpdateView):

    model = Asset_type
    fields = "__all__"

    def get(self,request,pk):
        asset = 'active'
        instance = Asset_type.objects.get(id=pk)
        form = Asset_Type_Form(instance=instance)
        return render(request, 'datas_update.html',{'asset':asset,'form':form})

    def get_success_url(self):
        return reverse('app:Asset-type')

class Asset_category_update_View(UpdateView):

    model = Asset_category
    fields = "__all__"

    def get(self,request,pk):
        asset = 'active'
        instance = Asset_category.objects.get(id=pk)
        form = Asset_Category_Form(instance=instance)
        return render(request, 'datas_update.html',{'asset':asset,'form':form})

    def get_success_url(self):
        return reverse('app:Asset-category')
