from django.forms import ModelForm,HiddenInput
from crispy_forms.helper import FormHelper
from django import forms


from datas.models.entity import *
from .entity_forms_helper import *


# Entity  Form class
class Entity_Form(ModelForm):

    class Meta:
        model = Entity
        fields = ['entity_FR','entity_type']


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Entity_FormSetHelper()
        self.helper.form_method = 'post'

class Entity_Type_Form(ModelForm):

    class Meta:
        model = Entity_type
        fields = ['entity_type_FR',]


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Entity_Type_FormSetHelper()
        self.helper.form_method = 'post'
