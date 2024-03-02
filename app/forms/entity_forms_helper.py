from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit, Row, Column



class Entity_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(

            Row(
                Column('entity_type', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('entity_FR', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True


class Entity_Type_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('entity_type_FR', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True
