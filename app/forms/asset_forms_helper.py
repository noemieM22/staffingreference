from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit, Row, Column



class Asset_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('label', css_class='form-group col-md-10 mb-0'),
                Column('type', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('host_name', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('login', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('password', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('sgbd', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True
