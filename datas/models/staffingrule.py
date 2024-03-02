from django.db import models

from .asset import *
from .entity import *
# models linked with staffing references rules

# Type : individuel, partagé, libre-service, opérationnel...
class Staffing_use_type(models.Model):

    staffing_use_type_FR = models.CharField("Dotation",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['staffing_use_type_FR'], name='unique Staffing_use_type')
        ]
    def __str__(self):
        return self.staffing_use_type_FR

class Staffing_rule(models.Model):
    staffing_rule_asset = models.ForeignKey(Asset, on_delete = models.PROTECT,related_name='staffing_rule_asset',verbose_name='Asset')
    staffing_rule_entity = models.ForeignKey(Entity, on_delete = models.PROTECT,related_name='staffing_rule_entity',verbose_name='Affectation')
    staffing_rule_type = models.ForeignKey(Staffing_use_type, on_delete = models.PROTECT,related_name='staffing_rule_type',verbose_name='Dotation')
    staffing_rule_count = models.SmallIntegerField("Nombre",null=False, blank = False)
    staffing_rule_comment = models.TextField("Précisions")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['staffing_rule_asset','staffing_rule_entity','staffing_rule_type'], name='unique Staffing_rule')
        ]
