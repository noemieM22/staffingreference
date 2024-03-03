from django import template
from datas.models import *

from datas.statics.datas_structure import get_fields

from django.apps import apps
from datas.models.entity import *

register = template.Library()

# list of objects for one table
@register.inclusion_tag("tags/staffingrules_list.html")
def show_staffingrules_list(title):
    # rules : {'Par catégorie',{'Catégorie A', [list]}}
    rules={}
    entity_type=Entity_type.objects.all()
    for ent_t in entity_type:
        entities= Entity.objects.filter(entity_type=ent_t)
        rules_detail={}

        for ent in entities:
            rules_byent= Staffing_rule.objects.filter(staffing_rule_entity=ent)
            rules_detail[ent.entity_FR]= rules_byent
        rules[ent_t.entity_type_FR]= rules_detail


    return { "title":title,'rules':rules}

# list of objects for one table
@register.inclusion_tag("tags/object_list.html")
def show_staffingrule_list(tableToDisplay,title, restrict):
    url_princ = tableToDisplay.replace('_','').lower()
    toSearch = Entity_type.objects.get(entity_type_FR = title)
    fields= get_fields(eval(tableToDisplay))
    lib = tableToDisplay.replace("_","").lower()+str(toSearch.id)
    if (toSearch):
        url = "/datas/"+ url_princ +"?staffing_rule_entity_type=" + str(toSearch.id)
    else:
        url = "/datas/"+ url_princ.lower() +"/"
    return {"urlasset": url,"lib":lib, "fields" : fields,"title":title}


#table of datas
@register.inclusion_tag("tags/object_list.html")
def show_object_list(tableToDisplay,title):
    url = "/datas/"+ tableToDisplay.replace('_','').lower() +'/'
    fields= get_fields(eval(tableToDisplay))
    lib = tableToDisplay.replace("_","").lower()
    return {"urlasset": url,"lib":lib, "fields" : fields,"title":title}
# ------------------------------------
# @register.filter(name="has_group")
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists()
