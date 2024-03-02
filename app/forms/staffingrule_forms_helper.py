from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit, Row, Column



class Staffing_rule_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('staffing_rule_asset', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('staffing_rule_entity', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('staffing_rule_type', css_class='form-group col-md-10 mb-0'),
            ),
            Row(
                Column('staffing_rule_count', css_class='form-group col-md-10 mb-0'),
            ),

            Row(
                Column('staffing_rule_comment', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True



class Staffing_use_type_FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout(
            Row(
                Column('staffing_use_type_FR', css_class='form-group col-md-10 mb-0'),
            ),
        )
        self.render_required_fields = True
