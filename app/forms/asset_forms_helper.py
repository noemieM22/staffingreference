from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit, Row, Column



class Asset_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('asset_category', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('asset_type', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('asset_FR', css_class='form-group col-md-10 mb-0'),
            ),

            Row(
                Column('asset_loan', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True


class Asset_Type_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('asset_type_FR', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True

class Asset_Category_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('asset_catgory_FR', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('asset_catgory_parent', css_class='form-group col-md-2 mb-0'),
            ),
        )
        self.render_required_fields = True
