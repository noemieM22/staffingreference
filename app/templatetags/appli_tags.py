from django import template
from datas.models import *

from datas.statics.datas_structure import get_fields

from django.apps import apps

register = template.Library()

# list of objects for one table
@register.inclusion_tag('tags/object_list.html')
def show_object_list(tableToDisplay):
    fields= get_fields(eval(tableToDisplay))
    lib = tableToDisplay.replace('_','').lower()
    url = '/datas/'+ lib +'/'
    return {'urlasset': url,'lib':lib, 'fields' : fields}




# ------------------------------------
# @register.filter(name='has_group')
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists()
