from django.forms import ModelForm,HiddenInput
from crispy_forms.helper import FormHelper
from django import forms


from datas.models import *
from .staffingrule_forms_helper import *


# Asset  Form class
class Staffing_rule_Form(ModelForm):

    class Meta:
        model = Staffing_rule
        # fields = ['staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']
        fields = ['staffing_rule_asset','staffing_rule_entity','staffing_rule_type','staffing_rule_count','staffing_rule_comment']

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Staffing_rule_FormSetHelper()
        self.helper.form_method = 'post'

class Staffing_use_type_Form(ModelForm):

    class Meta:
        model = Staffing_use_type
        fields = ['staffing_use_type_FR',]


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Staffing_use_type_FormSetHelper()
        self.helper.form_method = 'post'
