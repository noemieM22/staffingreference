from django.db import models

from .asset import *
from .entity import *
# models linked with staffing references rules

# Type : individuel, partagé, libre-service, opérationnel...
class Staffing_use_type(models.Model):

    staffing_use_type_FR = models.CharField("Utilisation",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['staffing_use_type_FR'], name='unique Staffing_use_type')
        ]


class Staffing_rule(models.Model):

    staffing_rule_asset = models.ForeignKey(Asset, on_delete = models.CASCADE,related_name='staffing_rule_asset')
    staffing_rule_entity = models.ForeignKey(Entity, on_delete = models.CASCADE,related_name='staffing_rule_entity')
    staffing_rule_type = models.ForeignKey(Staffing_use_type, on_delete = models.CASCADE,related_name='staffing_rule_type')
    staffing_rule_count = models.SmallIntegerField("Nombre",null=False, blank = False)
    staffing_rule_comment = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['staffing_rule_asset','staffing_rule_entity','staffing_rule_type'], name='unique Staffing_rule')
        ]
