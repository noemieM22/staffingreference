from django.forms import ModelForm,HiddenInput
from crispy_forms.helper import FormHelper
from django import forms


from datas.models.asset import *
from . asset_forms_helper import *

# Asset category Form class
class Asset_category_Form(ModelForm):

    class Meta:
        model = Asset_category
        fields = ['asset_category_FR','asset_category_level']


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Asset_FormSetHelper()
        self.helper.form_method = 'post'

# Asset  Form class
class Asset_Form(ModelForm):

    class Meta:
        model = Asset
        fields = ['asset_FR','asset_FR','asset_FR']


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Asset_FormSetHelper()
        self.helper.form_method = 'post'
