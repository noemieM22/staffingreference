from django import template
from datas.models import *



register = template.Library()

# ---------------ASSET
# liste des asset sous forme de tableau
@register.inclusion_tag('tags/asset_list.html')
def show_asset(type):
    return {'url':'/datas/asset/?type='+type,'type':type}



# ------------------------------------
# @register.filter(name='has_group')
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists()
