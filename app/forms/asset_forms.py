from django.forms import ModelForm,HiddenInput
from crispy_forms.helper import FormHelper
from django import forms


from datas.models.asset import *
from . asset_forms_helper import *


# Asset  Form class
class Asset_Form(ModelForm):

    class Meta:
        model = Asset
        fields = ['asset_category','asset_FR','asset_type','asset_loan']


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Asset_FormSetHelper()
        self.helper.form_method = 'post'

class Asset_Type_Form(ModelForm):

    class Meta:
        model = Asset_type
        fields = ['asset_type_FR',]


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Asset_Type_FormSetHelper()
        self.helper.form_method = 'post'

class Asset_Category_Form(ModelForm):

    class Meta:
        model = Asset_category
        fields = ['asset_category_FR','asset_category_parent']


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.helper = Asset_Type_FormSetHelper()
        self.helper.form_method = 'post'
